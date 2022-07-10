"""
    genre blueprint
    views
"""

# global imports
from flask import Blueprint, request


# local imports
from .models import GenreTop

bp_genre = Blueprint("bp_genre", __name__)


@bp_genre.route("/<string:genre>")
def index_genre_top(genre):
    """ Top 10 movies by genre route """
    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)

    return GenreTop(genre).jsonify(), 200
