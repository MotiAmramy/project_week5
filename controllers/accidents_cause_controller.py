from flask import Blueprint, jsonify
from database.connect import accidents_collection
accidents_cause_blueprint = Blueprint('accidents_cause', __name__)


@accidents_cause_blueprint.route('/accidents/cause/<area>', methods=['GET'])
def get_accidents_by_cause(area):
    pipeline = [
        {'$match': {'BEAT_OF_OCCURRENCE': area}},
        {'$group': {
            '_id': '$PRIM_CONTRIBUTORY_CAUSE',
            'count': {'$sum': 1}
        }}
    ]
    results = list(accidents_collection.aggregate(pipeline))
    return jsonify(results), 200
