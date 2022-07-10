"""
    Homework №14
    App data class
"""

# global imports
import sqlite3

# local imports
from grm import Singleton


class BaseAppData:
    """ Base app data class """
    _connection_str = None
    _connection = None

    def connect(self, connection_str):
        """ Save string connection """
        self._connection_str = connection_str

    def __enter__(self):
        """ For with """
        if not self._connection_str:
            raise RuntimeError("You must connect to the database first! Connection string is empty!")

        self._connection = sqlite3.Connection(self._connection_str)

        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ For with """
        if self._connection is not None:
            self._connection.close()
            self._connection = None


class AppData(BaseAppData, metaclass=Singleton):
    """ Data for hw14 """
    pass


class AppDataHW15(BaseAppData, metaclass=Singleton):
    """ Data for hw15 """
    pass
