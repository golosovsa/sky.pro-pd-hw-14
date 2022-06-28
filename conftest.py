"""
    conftest module
    fixtures for app testing
"""

# global imports
import os.path
import sqlite3

import pytest
from flask import Flask

# local imports
from app import create_app
import config


@pytest.fixture(scope="module")
def test_app():
    """ Fixture for testing the app """

    app: Flask = create_app()
    app.config.from_object(config.Testing)

    with app.app_context(), app.test_request_context():
        yield app


@pytest.fixture(scope="module")
def test_db_cursor():
    with sqlite3.connect(os.path.join(
            config.Testing.APP_DATA_FOLDER,
            config.Testing.APP_SQLITE_FILENAME
    )) as conn:
        yield conn.cursor()
