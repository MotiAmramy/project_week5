from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request
from database.connect import accidents_collection


period_area_blueprint = Blueprint('injuries_area', __name__)


@period_area_blueprint.route('/accidents/area/<area>/period', methods=['GET'])
def get_accidents_by_area_and_period(area):
    period = request.args.get('period', 'day')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    query = {
        'BEAT_OF_OCCURRENCE': area,
        'CRASH_DATE': {
            '$gte': start_date,
            '$lt': end_date + timedelta(days=1)  # Include end date
        }
    }
    accidents = list(accidents_collection.find(query))
    return jsonify(accidents), 200
