"""
    config package
    production app config class
"""

# from package imports
from .base import Base


class Production(Base):
    """ Production config for deploying """

    # app data config
    APP_DATA_FOLDER = "/home/golosovsa/data"

