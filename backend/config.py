"""AI Video Factory — configuration.

Centralized application configuration. Values are read from environment
variables at load time, each with a sensible default so the system runs
out of the box in development.

Uses only the Python standard library (no external dependencies).

Requires Python 3.11+.
"""

from __future__ import annotations

import os


class Config:
    """Application configuration loaded from environment variables.

    Each field falls back to a documented default when its environment
    variable is not set.
    """

    # Human-readable project name.
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "AI Video Factory")

    # Deployment environment: e.g. "development", "staging", "production".
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Logging verbosity: e.g. "DEBUG", "INFO", "WARNING", "ERROR".
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Filesystem path for working/structured data.
    DATA_PATH: str = os.getenv("DATA_PATH", "./data")

    # Filesystem path where model files/interfaces live.
    MODELS_PATH: str = os.getenv("MODELS_PATH", "./models")

    # Filesystem path for generated output (media, renders).
    OUTPUT_PATH: str = os.getenv("OUTPUT_PATH", "./output")


# Shared configuration instance for convenient import.
config = Config()
