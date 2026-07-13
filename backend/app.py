"""AI Video Factory — application bootstrap.

Wires together the core building blocks (configuration, logging, health
checks, and the :class:`~backend.main.VideoFactory`) and manages the
application lifecycle: initialize, start, and shutdown.

The business logic of the pipeline is not implemented yet. Where the
:class:`VideoFactory` skeleton raises :class:`NotImplementedError`, the
bootstrap degrades gracefully and logs the gap instead of crashing.

Uses only the Python standard library (no external dependencies).

Requires Python 3.11+.
"""

from __future__ import annotations

from backend.config import Config
from backend.health import HealthChecker
from backend.logger import LoggerFactory
from backend.main import VideoFactory


class Application:
    """Owns the application lifecycle and its core components."""

    def __init__(self) -> None:
        # Configuration is class-level; keep a reference for clarity.
        self.config = Config
        self.logger = LoggerFactory.create_logger("app")
        self.health_checker = HealthChecker()
        self.factory: VideoFactory | None = None
        self.running = False

    def initialize(self) -> dict:
        """Prepare the application.

        Runs health checks, logs a readable summary, and creates the
        VideoFactory instance. Returns the aggregated health-check result.
        """
        self.logger.info("Initializing %s...", self.config.PROJECT_NAME)

        results = self.health_checker.run_all_checks()
        self.logger.info("Health checks — overall: %s", results["overall"].upper())
        for check in results["checks"]:
            self.logger.info(
                "  [%s] %s: %s",
                check["status"].upper(),
                check["name"],
                check["detail"],
            )
        if results["overall"] == "error":
            self.logger.error("Health checks reported errors; startup may be unsafe.")

        self.factory = VideoFactory()
        self._try("VideoFactory.initialize", self.factory.initialize)
        return results

    def start(self) -> None:
        """Start the application, initializing it first if needed."""
        self.logger.info("Starting %s...", self.config.PROJECT_NAME)
        if self.factory is None:
            self.initialize()

        self.running = True
        self._try("VideoFactory.start", self.factory.start)
        self.logger.info("%s is running.", self.config.PROJECT_NAME)

    def shutdown(self) -> None:
        """Stop the application and release resources."""
        self.logger.info("Shutting down %s...", self.config.PROJECT_NAME)
        if self.factory is not None:
            self._try("VideoFactory.stop", self.factory.stop)
        self.running = False
        self.logger.info("Shutdown complete.")

    def _try(self, label: str, action) -> None:
        """Call a factory action, tolerating not-yet-implemented behavior."""
        try:
            action()
        except NotImplementedError:
            self.logger.warning("%s is not implemented yet.", label)
