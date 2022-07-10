"""
    rating blueprint
    views
"""

# global inputs
from flask import Blueprint, request, Response, jsonify
from werkzeug.exceptions import NotFound

# local imports
from .models import Rating

bp_rating = Blueprint("bp_rating", __name__)


@bp_rating.route("/<string:rating>", methods=["GET"])
def index_movies_by_rating(rating: str):
    """ Movies by rating route """
    ratings = {
        "children": ["G"],
        "family": ["G", "PG", "PG-13"],
        "adult": ["R", "NC-17"],
    }

    if rating not in ratings:
        return jsonify(None), 200

    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)

    return Rating(ratings[rating], limit, offset).jsonify(), 200
