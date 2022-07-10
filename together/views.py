"""
    together blueprint
    views
"""


# global imports
from flask import Blueprint, request


# local imports
from .models import Together


bp_together = Blueprint("bp_together", __name__)


@bp_together.route("/<string:actor1>/<string:actor2>")
def index_filmed_together_more_than(actor1, actor2):
    """ Actors who play together with two actors more than 2 times """
    limit = request.args.get("limit", 100)
    offset = request.args.get("offset", 0)
    times = request.args.get("times", 2)

    return Together(actor1, actor2, times, limit, offset).jsonify(), 200
