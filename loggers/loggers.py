"""
    loggers package
    loggers helper functions
"""

import logging
import os
from werkzeug.exceptions import InternalServerError


def init_loggers(app):
    """ Init app loggers

    1. Exception Errors level
    2. Api usage info
    3. User activity info

    """

    # formatters
    user_formatter = logging.Formatter("%(asctime)s : %(message)s")
    api_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    errors_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    # filenames
    logs_dir = app.config.get("APP_LOG_DIR", None)
    user_filename = app.config.get("APP_LOG_USER_ACTIVITY_FILE", None)
    api_filename = app.config.get("APP_LOG_API_USAGE_FILE", None)
    errors_filename = app.config.get("APP_LOG_EXCEPTION_ERRORS_FILE", None)

    if not logs_dir \
            or not user_filename \
            or not api_filename \
            or not errors_filename \
            or not os.path.isdir(logs_dir):
        raise InternalServerError("app logging definitions error")

    # file handlers
    user_file_handler = logging.FileHandler(os.path.join(logs_dir, user_filename))
    api_file_handler = logging.FileHandler(os.path.join(logs_dir, api_filename))
    errors_file_handler = logging.FileHandler(os.path.join(logs_dir, errors_filename))

    # User activity logger
    logger = logging.getLogger("user")
    logger.setLevel(logging.INFO)
    user_file_handler.setFormatter(user_formatter)
    logger.addHandler(user_file_handler)

    # API usage logger
    logger = logging.getLogger("api")
    logger.setLevel(logging.INFO)
    api_file_handler.setFormatter(api_formatter)
    logger.addHandler(api_file_handler)

    # API errors logger
    logger = logging.getLogger("errors")
    logger.setLevel(logging.ERROR)
    errors_file_handler.setFormatter(errors_formatter)
    logger.addHandler(errors_file_handler)
