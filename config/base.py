"""
    config package
    base app config class
"""


class Base:
    """ Base app config class """

    # app data config
    APP_DATA_FOLDER = ""
    APP_SQLITE_FILENAME = "netflix.db"

    # flask config
    JSON_AS_ASCII = False

    # logging config
    APP_LOG_DIR = "logs/"
    APP_LOG_EXCEPTION_ERRORS_FILE = "errors.log"
    APP_LOG_API_USAGE_FILE = "api.log"
    APP_LOG_USER_ACTIVITY_FILE = "user.log"
