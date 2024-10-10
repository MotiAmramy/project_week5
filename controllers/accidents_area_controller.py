from flask import Blueprint, jsonify
from database.connect import accidents_collection
from indexes.index_mongo import index_get_accidents_by_area


accidents_area_blueprint = Blueprint('accidents_area', __name__)


@accidents_area_blueprint.route('/accidents/area/<area>', methods=['GET'])
def get_accidents_by_area(area):
    try:
        accidents = list(accidents_collection.find({'BEAT_OF_OCCURRENCE': area}))
        index_get_accidents_by_area(area)
        return jsonify(len(accidents)), 200
    except Exception as e:
        return jsonify({'error': f"{e}"})