from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request
from database.connect import accidents_collection, daily_collection

period_area_blueprint = Blueprint('injuries_area', __name__)


@period_area_blueprint.route('/accidents/area/<area>/period', methods=['GET'])
def get_accidents_by_area_and_period(area):
    start_date = request.args.get('period')

    start_date = datetime.strptime(start_date, '%Y-%m-%d')

    query = {
        'BEAT_OF_OCCURRENCE': area,
        'CRASH_DATE': start_date
    }

    accidents = list(daily_collection.find(query))
    return jsonify(accidents), 200
