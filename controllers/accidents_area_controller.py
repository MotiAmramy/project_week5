from flask import Blueprint, jsonify

from database.connect import accidents_collection

accidents_area_blueprint = Blueprint('accidents_area', __name__)




@accidents_area_blueprint.route('/accidents/area/<area>', methods=['GET'])
def get_accidents_by_area(area):
    accidents = list(accidents_collection.find({'BEAT_OF_OCCURRENCE': area}))
    return jsonify(len(accidents)), 200
