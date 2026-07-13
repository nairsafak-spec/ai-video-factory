"""AI Video Factory — logging infrastructure.

Provides a small factory for creating consistently configured console
loggers. The default log level is taken from :class:`~backend.config.Config`.

Uses only the Python standard library (no external dependencies).

Requires Python 3.11+.
"""

from __future__ import annotations

import logging

from backend.config import Config

# Timestamp, log level, logger name, and message.
_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class LoggerFactory:
    """Factory for creating configured console loggers."""

    @staticmethod
    def create_logger(name: str) -> logging.Logger:
        """Create and return a console logger.

        The logger writes to stderr with a timestamp, level, name, and
        message. Its level defaults to ``Config.LOG_LEVEL``. Repeated calls
        with the same name do not add duplicate handlers.
        """
        logger = logging.getLogger(name)

        # Resolve the level from Config; fall back to INFO if invalid.
        level = logging.getLevelName(str(Config.LOG_LEVEL).upper())
        if not isinstance(level, int):
            level = logging.INFO
        logger.setLevel(level)

        # Avoid attaching multiple handlers to the same logger.
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter(_LOG_FORMAT, _DATE_FORMAT))
            logger.addHandler(handler)

        return logger
