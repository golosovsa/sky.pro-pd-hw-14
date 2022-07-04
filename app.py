"""
    Homework №14
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/14-SQL-19417ff81e514e78a183c5a49b2d5c39

    V1.0
"""

# global inputs
import dotenv
import os
from pathlib import Path
from flask import Flask, render_template
from werkzeug.exceptions import InternalServerError

# local imports
import config
import loggers
from app_data import AppData
from movie.views import bp_movie
from rating.views import bp_rating


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
        raise InternalServerError("The APP_CONFIG application environment name does not exist.\n"
                                  "Make sure that the .env file is correct or exists.")

    # app data
    database_connection_str = \
        Path(the_app.config.get("APP_DATA_FOLDER", "")) / the_app.config.get("APP_SQLITE_FILENAME", "")
    AppData().connect(database_connection_str)

    # logging
    loggers.init(the_app)

    # blueprints
    the_app.register_blueprint(bp_movie, url_prefix="/movie/")
    the_app.register_blueprint(bp_rating, url_prefix="/rating/")

    # static root route
    @the_app.route("/", methods=["GET"])
    def index_root():
        return the_app.send_static_file("index.html")

    # error handlers

    return the_app


if __name__ == '__main__':
    create_app().run()
