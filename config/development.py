"""
    config package
    development app config class
"""


# from package imports
from .base import Base


class Development(Base):
    """ Development config for internal flask wsgi server """

    # app data config
    APP_DATA_FOLDER = "./data"

