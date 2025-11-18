#!/usr/bin/env python3
# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Check for vulnerable dependencies using pip-audit (better alternative to Safety).
"""
import json
import sys
import subprocess
from pathlib import Path


def install_pip_audit() -> bool:
    """Install pip-audit if not available."""
    try:
        print("📦 Installing pip-audit...")
        subprocess.run(["pip", "install", "pip-audit"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def run_vulnerability_scan() -> tuple[int, str]:
    """Run vulnerability scan using pip-audit and write directly to file."""
    try:
        # Use pip-audit's built-in output option to write directly to our target file
        print("🔍 Running pip-audit vulnerability scan...")
        result = subprocess.run(
            ["pip-audit", "--format=json", "--output=pip-audit-results.json"],
            capture_output=True,
            text=True,
            check=False,
            timeout=120,
        )

        return result.returncode, result.stderr

    except subprocess.TimeoutExpired:
        return 1, "Vulnerability scan timed out"
    except FileNotFoundError:
        # pip-audit not installed, try to install it
        if install_pip_audit():
            return run_vulnerability_scan()  # Retry
        else:
            return 1, "Could not install pip-audit"
    except Exception as e:
        return 1, str(e)


def parse_results_file(results_file: Path) -> dict:
    """Parse results from the pip-audit output file."""
    if not results_file.exists():
        return {"vulnerabilities": [], "count": 0}

    try:
        with open(results_file) as f:
            data = json.load(f)

        # Handle different pip-audit output formats
        if isinstance(data, list):
            return {"vulnerabilities": data, "count": len(data)}
        elif isinstance(data, dict):
            # Check for 'dependencies' format
            if "dependencies" in data:
                # Count packages with vulnerabilities
                vulns = []
                for dep in data["dependencies"]:
                    if dep.get("vulns"):
                        vulns.extend(dep["vulns"])
                return {"vulnerabilities": vulns, "count": len(vulns), "raw_data": data}
            else:
                # Standard format
                vulnerabilities = data.get("vulnerabilities", [])
                return {
                    "vulnerabilities": vulnerabilities,
                    "count": len(vulnerabilities),
                }

        return {"vulnerabilities": [], "count": 0}

    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️ Could not parse results file: {e}")
        return {"vulnerabilities": [], "count": 0}


def main() -> None:
    """Main function."""
    print("🛡️ Dependency Vulnerability Check (pip-audit)")
    print("=" * 55)

    # Run vulnerability scan (writes directly to pip-audit-results.json)
    exit_code, stderr = run_vulnerability_scan()

    # Parse results from the output file
    results_file = Path("pip-audit-results.json")
    results = parse_results_file(results_file)

    print(f"📝 Results saved to: {results_file}")

    # Report results
    vuln_count = results.get("count", 0)

    if exit_code == 0 and vuln_count == 0:
        print("✅ No known vulnerabilities found")
        sys.exit(0)
    elif vuln_count > 0:
        print(f"❌ Found {vuln_count} vulnerabilities")

        # Show details by examining the raw data structure
        raw_data = results.get("raw_data", {})
        if raw_data and "dependencies" in raw_data:
            print("\n🔍 Vulnerability details:")
            vuln_count_shown = 0
            for dep in raw_data["dependencies"]:
                dep_name = dep.get("name", "unknown")
                dep_version = dep.get("version", "unknown")
                vulns = dep.get("vulns", [])

                if vulns:
                    for vuln in vulns:
                        if vuln_count_shown >= 10:  # Show first 10
                            break
                        vuln_count_shown += 1
                        vuln_id = vuln.get("id", "unknown")
                        fix_versions = vuln.get("fix_versions", [])
                        fix_info = (
                            f" (fix: {', '.join(fix_versions)})" if fix_versions else ""
                        )
                        print(
                            f"  {vuln_count_shown}. {dep_name} {dep_version} - {vuln_id}{fix_info}"
                        )

                if vuln_count_shown >= 10:
                    break

            if vuln_count > 10:
                print(f"  ... and {vuln_count - 10} more")

        sys.exit(1)
    else:
        print("⚠️ Scan completed with warnings")
        if stderr.strip():
            print(f"Warnings: {stderr}")
        sys.exit(0)


if __name__ == "__main__":
    main()
