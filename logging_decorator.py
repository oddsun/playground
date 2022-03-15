import json
import logging
import logging.config
import os
from functools import wraps
from inspect import getframeinfo, stack


def setup_logging(
        name,
        default_path='config/logging.json',
        default_level=None,
        env_key='LOG_CFG',
):
    """Setup logging configuration

    """
    if not os.path.exists('log'):
        os.mkdir('log')
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    logger = logging.getLogger(name)
    return logger


class CustomFormatter(logging.Formatter):
    """ Custom Formatter does these 2 things:
    1. Overrides 'funcName' with the value of 'func_name_override', if it exists.
    2. Overrides 'filename' with the value of 'file_name_override', if it exists.
    """

    def format(self, record):
        if hasattr(record, 'name_override'):
            record.funcName = record.name_override
        if hasattr(record, 'file_override'):
            record.filename = record.file_override
        if hasattr(record, 'line_override'):
            record.lineno = record.line_override
        return super(CustomFormatter, self).format(record)


logger = setup_logging(__name__)


def log(statement):
    def decorator(func):
        caller = getframeinfo(stack()[1][0])

        @wraps(func)
        def wrapper(*args, **kwargs):
            extra = {
                'name_override': func.__name__,
                'file_override': os.path.basename(caller.filename),
                'line_override': caller.lineno
            }
            # set name_override to func.__name__
            logger.info(statement, extra=extra)
            logger.info('starting', extra=extra)
            logger.info(f'{args=}, {kwargs=}', extra=extra)
            result = func(*args, **kwargs)

            logger.info(f'{result=}', extra=extra)

            logger.info('completed', extra=extra)
            return result

        return wrapper

    return decorator
