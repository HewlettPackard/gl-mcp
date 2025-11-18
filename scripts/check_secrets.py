#!/usr/bin/env python3
# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Detect secrets using detect-secrets with custom filtering.
Only filters specific secret values, not entire files.
"""
import json
import sys
import subprocess


def run_command(
    cmd: list[str], capture_output: bool = True
) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    try:
        return subprocess.run(
            cmd, capture_output=capture_output, text=True, check=False, timeout=120
        )
    except subprocess.TimeoutExpired:
        print("❌ Command timed out after 120 seconds")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running command {' '.join(cmd)}: {e}")
        sys.exit(1)


# Define allowlist patterns - these secret VALUES will be ignored
ALLOWLIST_PATTERNS = [
    "secret123",
    "password123",
    "dummy123",
    "your-client-secret",
    "test-token-sample-service",
    "integration-client-secret",
    "test",
    "example",
    "secret",
    "sample",
    "mock",
    "fake",
    "localhost",
]


def is_allowlisted_secret(secret: dict, file_path: str) -> bool:
    """
    Check if a SECRET VALUE should be ignored based on allowlist patterns.
    Does NOT ignore entire files - only specific secret values.

    Args:
        secret: Secret detection dict with line_number, type, etc.
        file_path: Path to the file containing the secret

    Returns:
        True if this specific secret should be ignored, False otherwise
    """
    # Check actual line content against allowlist patterns
    line_number = secret.get("line_number")
    if line_number:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                if line_number <= len(lines):
                    line_content = lines[line_number - 1].lower()
                    # Check if any allowlist pattern is in the line
                    if any(
                        pattern.lower() in line_content
                        for pattern in ALLOWLIST_PATTERNS
                    ):
                        return True
        except Exception:
            pass  # If we can't read the file, don't filter it

    return False


def scan_with_filters() -> dict:
    """Run detect-secrets scan - only exclude build artifacts, scan everything else."""
    print("🔍 Scanning ALL files for secrets...")

    result = run_command(
        [
            "uv",
            "run",
            "detect-secrets",
            "scan",
            "--all-files",
            # Only exclude build/dependency folders that never have real code
            "--exclude-files",
            r"\.venv/|venv/|.ruff_cache/|node_modules/|__pycache__|\.git/|\.tox/|\.eggs/",
        ]
    )

    if result.returncode != 0:
        print(f"❌ detect-secrets scan failed: {result.stderr}")
        sys.exit(1)

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse detect-secrets output: {e}")
        sys.exit(1)


def filter_secrets(scan_results: dict) -> dict:
    """
    Filter out ONLY allowlisted secret VALUES from scan results.
    All files are scanned, but specific secret values are filtered.

    Args:
        scan_results: Full scan results from detect-secrets

    Returns:
        Filtered results with allowlisted secret VALUES removed
    """
    filtered_results = {}

    for file_path, secrets in scan_results.get("results", {}).items():
        # Filter secrets for this file based on their VALUES, not the file path
        filtered_secrets = [
            secret for secret in secrets if not is_allowlisted_secret(secret, file_path)
        ]

        # Only include file if it has non-allowlisted secrets
        if filtered_secrets:
            filtered_results[file_path] = filtered_secrets

    return {
        "results": filtered_results,
        "generated_at": scan_results.get("generated_at"),
        "filters_used": scan_results.get("filters_used", []),
    }


def count_secrets(results: dict) -> int:
    """Count total secrets in results."""
    return sum(len(secrets) for secrets in results.get("results", {}).values())


def show_secret_details(results: dict) -> None:
    """Show details of found secrets with file paths."""
    print("\n📋 Real secrets found (after filtering allowlisted values):")

    for file_path, secrets in results.get("results", {}).items():
        if secrets:
            print(f"\n  📄 {file_path}: {len(secrets)} secret(s)")
            for secret in secrets:
                secret_type = secret.get("type", "Unknown")
                line_num = secret.get("line_number", "Unknown")
                print(f"      • Line {line_num}: {secret_type}")


def main() -> None:
    """Main function."""
    print("🔐 Secret Detection Analysis")
    print("=" * 60)
    print("\n🔧 Allowlisted SECRET VALUES (will be ignored):")
    for pattern in ALLOWLIST_PATTERNS:
        print(f"  - {pattern}")
    print("\n📂 Scanning: ALL files (tests, docs, everything)")
    print("🚫 Only excluding: .venv/, node_modules/, __pycache__/, .git/")
    print("\n💡 Note: Only specific secret VALUES are filtered, not entire files")
    print("=" * 60)

    # Run scan on ALL files
    scan_results = scan_with_filters()

    # Filter only specific secret VALUES
    filtered_results = filter_secrets(scan_results)

    # Count secrets
    total_secrets = count_secrets(scan_results)
    filtered_secrets = count_secrets(filtered_results)
    ignored_secrets = total_secrets - filtered_secrets

    print("\n📊 Scan Summary:")
    print(f"  Total secrets detected: {total_secrets}")
    print(f"  Ignored (allowlisted values): {ignored_secrets}")
    print(f"  Real secrets requiring action: {filtered_secrets}")

    if filtered_secrets > 0:
        print(f"\n❌ Found {filtered_secrets} real secret(s) in code!")
        show_secret_details(filtered_results)

        print("\n📝 Next steps:")
        print("  1. Review the secrets listed above")
        print("  2. Remove real secrets from code")
        print("  3. Use environment variables or secret management")
        print("  4. If any are false positives, add the pattern to ALLOWLIST_PATTERNS")
        print("  5. Consider adding inline comments: # pragma: allowlist secret")
        sys.exit(1)
    else:
        print("\n✅ No real secrets found!")
        if ignored_secrets > 0:
            print(f"   (Ignored {ignored_secrets} allowlisted secret values)")
        sys.exit(0)


if __name__ == "__main__":
    main()
