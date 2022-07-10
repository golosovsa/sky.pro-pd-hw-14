"""
    animals blueprint
    views
"""


# global inputs
from flask import Blueprint


# local imports
from .models import Animal


bp_animals = Blueprint("bp_animals", __name__)


@bp_animals.route("/<int:pk>")
def index_animals_by_id(pk):
    """ Animal by id route """
    return Animal(pk).jsonify(), 200
