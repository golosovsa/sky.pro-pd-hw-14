"""
    together blueprint
    views
"""


# global imports
from flask import Blueprint


bp_together = Blueprint("bp_together", __name__)


@bp_together.route("/<string:actor1>/<string:actor2>")
def index_filmed_together_more_than(actor1, actor2):

    return f"index_filmed_together_more_than {actor1} {actor2}"
