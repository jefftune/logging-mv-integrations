import logging
from logging_mv_integrations import (TuneLoggingFormat, get_logger, __version__)

tune_logger = get_logger(
    logger_name=__name__, logger_version=__version__, logger_format=TuneLoggingFormat.JSON, logger_level=logging.DEBUG
)

tune_logger.info("logging: info", extra={'test': __name__})
tune_logger.debug("logging: debug", extra={'test': __name__})
tune_logger.warning("logging: warning", extra={'test': __name__})
tune_logger.error("logging: error", extra={'test': __name__})
tune_logger.critical("logging: critical", extra={'test': __name__})
tune_logger.exception("logging: exception", extra={'test': __name__})
