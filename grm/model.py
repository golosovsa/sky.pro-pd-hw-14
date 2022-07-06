"""
    GRM package
    Model base class
"""

# global imports
from flask import jsonify


class BaseModel:

    _data = None

    def jsonify(self):
        return jsonify(self._data)
