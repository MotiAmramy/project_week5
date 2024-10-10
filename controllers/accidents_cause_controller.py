from flask import Blueprint, jsonify
from database.connect import accidents_collection
from indexes.index_mongo import index_get_accidents_by_cause

accidents_cause_blueprint = Blueprint('accidents_cause', __name__)


@accidents_cause_blueprint.route('/accidents/cause/<area>', methods=['GET'])
def get_accidents_by_cause(area):
    try:
        pipeline = [
            {'$match': {'BEAT_OF_OCCURRENCE': area}},
            {'$group': {
                '_id': '$PRIM_CONTRIBUTORY_CAUSE',
                'count': {'$sum': 1}
            }}
        ]
        index_get_accidents_by_cause(area)
        results = list(accidents_collection.aggregate(pipeline))
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": f"{e}"})
