"""
    rating blueprint
    views
"""

# global inputs
from flask import Blueprint, request, Response
from werkzeug.exceptions import NotFound

# local imports
from .models import RatingModel

bp_rating = Blueprint("bp_rating", __name__)


@bp_rating.route("/<rating>", methods=["GET"])
def index_single_by_title(rating: str):

    ratings = {
              "children": ("G",),
              "family": ("G", "PG", "PG-13"),
              "adult": ("R", "NC-17"),
    }

    if rating not in ratings:
        return Response("[]", mimetype="application/json", status=200)

    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)

    return Response(RatingModel(ratings[rating], limit, offset))
