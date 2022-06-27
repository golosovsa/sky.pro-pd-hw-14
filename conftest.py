"""
    conftest module
    fixtures for app testing
"""

# global imports
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
