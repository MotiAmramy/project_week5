from flask import Blueprint
from database.connect import accidents_collection
from repository.utils import parse_json



injuries_area_blueprint = Blueprint('injuries_area', __name__)


@injuries_area_blueprint.route('/injuries/area/<area>', methods=['GET'])
def get_injury_statistics(area):
    pipeline = [
        {'$match': {'BEAT_OF_OCCURRENCE': area}},
        {'$group': {
            '_id': None,
            'total_injuries': {'$sum': '$injuries.INJURIES_TOTAL'},
            'fatal_injuries': {'$sum': '$injuries.fatal'},
            'non_fatal_injuries': {'$sum': '$injuries.non_fatal'}
        }}
    ]
    stats = accidents_collection.aggregate(pipeline)
    return parse_json(stats)[0], 200
