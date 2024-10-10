from flask import Blueprint, jsonify
from database.connect import accidents_collection
from indexes.index_mongo import index_get_injury_statistics
from repository.utils import parse_json



injuries_area_blueprint = Blueprint('injuries_area', __name__)


@injuries_area_blueprint.route('/injuries/area/<area>', methods=['GET'])
def get_injury_statistics(area):
    try:
        pipeline = [
            {'$match': {'BEAT_OF_OCCURRENCE': area}},
            {'$group': {
                '_id': None,
                'total_injuries': {'$sum': '$injuries.INJURIES_TOTAL'},
                'fatal_injuries': {'$sum': '$injuries.fatal'},
                'non_fatal_injuries': {'$sum': '$injuries.non_fatal'}
            }}
        ]
        index_get_injury_statistics(area)
        stats = accidents_collection.aggregate(pipeline)
        return parse_json(stats)[0], 200
    except Exception as e:
        return jsonify({"error": f"{e}"})
