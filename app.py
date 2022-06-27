"""
    Homework №14
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/14-SQL-19417ff81e514e78a183c5a49b2d5c39

    V1.0
"""


# global inputs
import dotenv
import os
from flask import Flask, render_template
from werkzeug.exceptions import InternalServerError


# local imports
import config


def create_app():

    the_app = Flask(__name__, static_folder="static", template_folder="templates")

    # place APP_CONFIG="production" in file .env before deploy
    dotenv.load_dotenv(override=True)
    app_config = os.environ.get("APP_CONFIG", None)

    if app_config == "development":
        the_app.config.from_object(config.Development)

    elif app_config == "production":
        the_app.config.from_object(config.Production)

    else:
        raise InternalServerError("The APP_CONFIG application environment variable does not exist.\n"
                                  "Make sure that the .env file is correct or exists.")

    # logging
    


if __name__ == '__main__':
    app.run()
