"""
    blueprint search
    views
"""


# global imports
from flask import Blueprint, request


# local imports
from .models import Search


bp_search = Blueprint("bp_search", __name__)


@bp_search.route("/<string:movie_type>/<int:release_year>/<string:genre>")
def index_search_by_type_release_genre(movie_type, release_year, genre):
    """ Search movies route """
    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)

    return Search(movie_type, release_year, genre, limit, offset).jsonify(), 200
