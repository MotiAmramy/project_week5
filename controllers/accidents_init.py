from flask import Blueprint, jsonify
from repository.csv_repository import init_chicago_car_accidents

accidents_init_blueprint = Blueprint('accidents_init', __name__)


@accidents_init_blueprint.route('/accidents/init', methods=['GET'])
def get_accidents_init():
    try:
        init_chicago_car_accidents()
        return jsonify({"success": "OK"})
    except Exception as e:
        return jsonify({'error': e}), 200

