"""
    movie blueprint
    views
"""


# global inputs
from flask import Blueprint, request

# local imports
from .models import Single, Short


bp_movie = Blueprint("bp_movie", __name__)


@bp_movie.route("/<string:title>", methods=["GET"])
def index_single_by_title(title: str):
    """ Single movie by id route """
    return Single(title).jsonify(), 200


@bp_movie.route("/<int:start>/to/<int:end>", methods=["GET"])
def index_short_by_range(start, end):
    """ Short data movies by years range """
    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)

    return Short(start, end, limit, offset).jsonify(), 200

