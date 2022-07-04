"""
    movie blueprint
    views
"""


# global inputs
from flask import Blueprint, request, Response


# local inputs
from .models import SingleModel, ShortModel

bp_movie = Blueprint("bp_movie", __name__)


@bp_movie.route("/<title>", methods=["GET"])
def index_single_by_title(title: str):
    return Response(SingleModel(title).result, mimetype="application/json", status=200)


@bp_movie.route("/<int:start>/to/<int:end>", methods=["GET"])
def index_short_by_range(start, end):

    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)

    return Response(ShortModel(start, end, limit, offset).result, mimetype="application/json", status=200)

