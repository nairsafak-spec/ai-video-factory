"""AI Video Factory — health checks.

Lightweight startup diagnostics that verify the runtime environment before
the system does real work. Each check returns a structured dictionary so the
results are easy to log, serialize, or surface in a dashboard.

Uses only the Python standard library (no external dependencies).

Requires Python 3.11+.
"""

from __future__ import annotations

import os
import platform
import shutil
import sys

from backend.config import Config

# Minimum supported Python version.
_MIN_PYTHON = (3, 11)

# Warn when free disk space drops below this many gigabytes.
_MIN_FREE_GB = 5.0


class HealthChecker:
    """Runs environment health checks and returns structured results."""

    def check_python_version(self) -> dict:
        """Verify the running Python version meets the minimum requirement."""
        current = sys.version_info
        ok = (current.major, current.minor) >= _MIN_PYTHON
        return {
            "name": "python_version",
            "status": "ok" if ok else "error",
            "detail": (
                f"Python {current.major}.{current.minor}.{current.micro}"
                + ("" if ok else f" (requires >= {_MIN_PYTHON[0]}.{_MIN_PYTHON[1]})")
            ),
            "data": {
                "version": f"{current.major}.{current.minor}.{current.micro}",
                "required": f"{_MIN_PYTHON[0]}.{_MIN_PYTHON[1]}",
            },
        }

    def check_disk_space(self) -> dict:
        """Report free disk space for the data path (or current directory)."""
        path = Config.DATA_PATH if os.path.isdir(Config.DATA_PATH) else os.getcwd()
        try:
            usage = shutil.disk_usage(path)
        except OSError as exc:
            return {
                "name": "disk_space",
                "status": "error",
                "detail": f"Could not read disk usage for {path}: {exc}",
                "data": {"path": path},
            }

        free_gb = usage.free / (1024 ** 3)
        total_gb = usage.total / (1024 ** 3)
        ok = free_gb >= _MIN_FREE_GB
        return {
            "name": "disk_space",
            "status": "ok" if ok else "warning",
            "detail": f"{free_gb:.2f} GB free of {total_gb:.2f} GB at {path}",
            "data": {
                "path": path,
                "free_gb": round(free_gb, 2),
                "total_gb": round(total_gb, 2),
                "min_free_gb": _MIN_FREE_GB,
            },
        }

    def check_environment(self) -> dict:
        """Report the active configuration/environment settings."""
        return {
            "name": "environment",
            "status": "ok",
            "detail": (
                f"{Config.ENVIRONMENT} environment, log level {Config.LOG_LEVEL}"
            ),
            "data": {
                "project_name": Config.PROJECT_NAME,
                "environment": Config.ENVIRONMENT,
                "log_level": Config.LOG_LEVEL,
                "data_path": Config.DATA_PATH,
                "models_path": Config.MODELS_PATH,
                "output_path": Config.OUTPUT_PATH,
                "platform": platform.platform(),
            },
        }

    def run_all_checks(self) -> dict:
        """Run every check and return an aggregated result with overall status."""
        checks = [
            self.check_python_version(),
            self.check_disk_space(),
            self.check_environment(),
        ]

        if any(c["status"] == "error" for c in checks):
            overall = "error"
        elif any(c["status"] == "warning" for c in checks):
            overall = "warning"
        else:
            overall = "ok"

        return {
            "overall": overall,
            "checks": checks,
        }
