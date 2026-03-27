import logging

logger = logging.getLogger("web_intelligence")
logger.addHandler(logging.NullHandler())


def setup_logging(level: int = logging.INFO, fmt: str | None = None) -> None:
    if fmt is None:
        fmt = "[%(levelname)s] web_intelligence.%(name)s: %(message)s"

    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
    logger.setLevel(level)
