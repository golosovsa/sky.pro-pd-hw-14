"""
    Homework №14
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/14-SQL-19417ff81e514e78a183c5a49b2d5c39

    V1.0
"""

# global inputs
from flask import Flask, render_template

# local imports
from app_data import AppData
from movie.views import bp_movie
from rating.views import bp_rating
from genre.views import bp_genre
from together.views import bp_together


def create_app():
    the_app = Flask(__name__, static_folder="static", template_folder="templates")

    # flask settings
    the_app.config.update({
        "JSON_AS_ASCII": False,
    })

    # app data
    AppData().connect("data/netflix.db")

    # blueprints
    the_app.register_blueprint(bp_movie, url_prefix="/movie/")
    the_app.register_blueprint(bp_rating, url_prefix="/rating/")
    the_app.register_blueprint(bp_genre, url_prefix="/genre/")
    the_app.register_blueprint(bp_together, url_prefix="/together/")

    # static root route
    @the_app.route("/", methods=["GET"])
    def index_root():
        return the_app.send_static_file("index.html")

    return the_app


if __name__ == '__main__':
    create_app().run()
