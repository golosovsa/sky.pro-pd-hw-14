"""
    config package
    testing app config class
"""


# from package imports
from .base import Base


class Testing(Base):
    """ Testing config for pytest """

    # app data config
    APP_DATA_FOLDER = "./data"

    # pytest settings
    TESTING = True
