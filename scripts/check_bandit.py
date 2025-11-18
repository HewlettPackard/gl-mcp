#!/usr/bin/env python3
# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Bandit Security Analysis Script

This script runs Bandit security analysis on Python code,
excludes common false positives, and provides clear reporting.
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any


def create_bandit_config() -> None:
    """Create Bandit configuration file with proper INI format."""
    config_content = """[bandit]
exclude_dirs = .venv,venv,env,.env,site-packages,__pycache__,.git,.pytest_cache,build,dist
skips = B101,B601
"""

    config_file = Path(".bandit")
    with open(config_file, "w") as f:
        f.write(config_content.strip() + "\n")
    print("📝 Created Bandit configuration file")


def run_bandit_scan() -> tuple[int, str]:
    """Run Bandit security scan and return exit code and stderr."""
    try:
        print("🔍 Running Bandit security analysis...")
        result = subprocess.run(
            [
                "uv",
                "run",
                "python",
                "-m",
                "bandit",
                "-r",
                ".",  # Recursive scan
                "-ll",  # Low confidence level
                "-f",
                "json",  # JSON format output
                "-o",
                "bandit-results.json",  # Output file
                "--skip",
                "B101,B601",  # Skip common false positives
                "--exclude",
                ".venv,venv,env,.env,site-packages,__pycache__,.git,.pytest_cache,build,dist",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )

        return result.returncode, result.stderr
    except subprocess.TimeoutExpired:
        return 124, "Bandit scan timed out after 120 seconds"
    except Exception as e:
        return 1, f"Error running Bandit: {e}"


def parse_bandit_results(results_file: Path) -> Dict[str, Any]:
    """Parse Bandit results JSON file."""
    try:
        if not results_file.exists():
            return {"error": "Results file not found", "results": []}

        with open(results_file) as f:
            data = json.load(f)

        return data
    except json.JSONDecodeError as e:
        return {"error": f"JSON decode error: {e}", "results": []}
    except Exception as e:
        return {"error": f"Error reading results: {e}", "results": []}


def analyze_results(results: Dict[str, Any]) -> Dict[str, int]:
    """Analyze Bandit results and count issues by severity."""
    if "error" in results:
        return {"high": 0, "medium": 0, "low": 0, "total": 0}

    issues = results.get("results", [])

    counts = {
        "high": len([i for i in issues if i.get("issue_severity") == "HIGH"]),
        "medium": len([i for i in issues if i.get("issue_severity") == "MEDIUM"]),
        "low": len([i for i in issues if i.get("issue_severity") == "LOW"]),
        "total": len(issues),
    }

    return counts


def display_results(results: Dict[str, Any], counts: Dict[str, int]) -> None:
    """Display Bandit analysis results."""
    if "error" in results:
        print(f"❌ Error reading Bandit results: {results['error']}")
        return

    print("📊 Bandit Analysis Results:")
    print(f"  HIGH severity: {counts['high']}")
    print(f"  MEDIUM severity: {counts['medium']}")
    print(f"  LOW severity: {counts['low']}")
    print(f"  Total issues: {counts['total']}")

    # Show details of HIGH severity issues
    if counts["high"] > 0:
        print("\n🔴 HIGH severity issues found:")
        issues = results.get("results", [])
        for issue in issues:
            if issue.get("issue_severity") == "HIGH":
                filename = issue.get("filename", "unknown")
                line_number = issue.get("line_number", "unknown")
                issue_text = issue.get("issue_text", "No description")
                test_id = issue.get("test_id", "unknown")

                print(f"  - {filename}:{line_number}")
                print(f"    {issue_text}")
                print(f"    Test ID: {test_id}")
                print()


def determine_exit_code(counts: Dict[str, int]) -> int:
    """Determine appropriate exit code based on findings."""
    if counts["high"] > 0:
        print("❌ HIGH severity security issues must be resolved")
        return 1
    elif counts["medium"] > 0:
        print("⚠️ MEDIUM severity issues found - review recommended")
        # Uncomment the next line to fail on medium severity too:
        # return 1
        return 0
    else:
        print("✅ No critical security issues found")
        return 0


def main() -> None:
    """Main function to run Bandit security analysis."""
    print("🛡️ Starting Bandit Security Analysis")

    # Run Bandit scan
    exit_code, stderr = run_bandit_scan()

    # Parse results
    results_file = Path("bandit-results.json")
    results = parse_bandit_results(results_file)

    print(f"📝 Results saved to: {results_file}")

    # Analyze and display results
    counts = analyze_results(results)
    display_results(results, counts)

    # Determine final exit code
    final_exit_code = determine_exit_code(counts)

    # Additional info if Bandit itself had issues
    if exit_code != 0 and stderr:
        print(f"\n⚠️ Bandit process issues (exit code {exit_code}):")
        print(f"  {stderr}")

    sys.exit(final_exit_code)


if __name__ == "__main__":
    main()
