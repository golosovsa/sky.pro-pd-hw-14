"""
    blueprint usage
    views
"""


# global imports
from flask import Blueprint, jsonify


bp_usage = Blueprint("bp_usage", __name__)


@bp_usage.route("/hw14")
def index_usage():
    """ Usage route for hw14 """
    usage_msg = [

        {'message': 'Hello from SKY.PRO lesson 14 homework project API )))'},
        {'message': 'You can use following api routes:'},
        {
            'message': '- this message',
            'route': '/usage/hw14'
        },
        {
            'message': '- get latest movie by title',
            'route': '/movie/<string:title>'
        },
        {
            'message': '- get movies by period',
            'route': '/movie/<int:start>/to/<int:end>[?limit=<int:limit>[&offset=<int:offset>]]'
        },
        {
            'message': '- get movies by rating',
            'route': '/rating/<string:rating=(children | family | adult)>[?limit=<int:limit>[&offset=<int:offset>]]'
        },
        {
            'message': '- get movies by genre',
            'route': '/genre/<string:genre>[?limit=<int:limit>[&offset=<int:offset>]]'
        },
        {
            'message': '- which of the actors plays more than 2 times with <actor1> and <actor2>',
            'route': '/together/<string:actor1>/<string:actor2>'
                     '[?limit=<int:limit>[&offset=<int:offset>[&times=<int:times>]]]'
        },
        {
            'message': 'search movie by <movie_type>, <release_year>, <genre>',
            'route': '/search/<string:movie_type>/<int:release_year>/<string:genre>'
                     '[?limit=<int:limit>[&offset=<int:offset>]]'
        },
    ]
    
    return jsonify(usage_msg), 200


@bp_usage.route("/hw15")
def index_usage_hw15():
    """ Usage route for hw15 """
    usage_msg = [

        {'message': 'Hello from SKY.PRO lesson 15 homework project API )))'},
        {'message': 'You can use following api routes:'},
        {
            'message': '- this message',
            'route': '/usage/hw15'
        },
        {
            'message': '- get information about animal by pk',
            'route': '<int:pk>'
        },
    ]

    return jsonify(usage_msg), 200
