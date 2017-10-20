#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import logging
from pprintpp import pprint
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)

log = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_format=LoggingFormat.STANDARD,
    logger_output=LoggingOutput.FILE
)

log.info("logging: info", extra={'test': __name__})
log.note("logging: note", extra={'test': __name__})
log.debug("logging: debug", extra={'test': __name__})
log.warning("logging: warning", extra={'test': __name__})
log.error("logging: error", extra={'test': __name__})
log.critical("logging: critical", extra={'test': __name__})
log.exception("logging: exception", extra={'test': __name__})

pprint(f"Logger file path: {log.logger_path}")

logger_fp = open(log.logger_path,'r')
pprint(logger_fp.readlines())

pprint(log.getLevelName())
