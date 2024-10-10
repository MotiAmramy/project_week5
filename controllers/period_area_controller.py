from datetime import datetime
from flask import Blueprint, jsonify
from database.connect import daily_collection, monthly_collection
from repository.csv_repository import extract_the_month
from repository.utils import find_the_day, parse_json, find_the_week

period_area_blueprint = Blueprint('period_area', __name__)


@period_area_blueprint.route('/accidents/area/<area>/date/<date>', methods=['GET'])
def get_accidents_by_area_and_date(area, date):
    day_accidents =  find_the_day(date, area)

    if not day_accidents:
        return jsonify({"message": "No accidents found for this area and date."}), 404

    return parse_json(day_accidents), 200



@period_area_blueprint.route('/accidents/area/<area>/month/<int:month>', methods=['GET'])
def get_accidents_by_area_and_month(area, month):
    month_accidents =  { 'area' : area, 'month': month}
    my_month_res = monthly_collection.find_one(month_accidents)
    if not my_month_res:
        return jsonify({"message": "No accidents found for this area and date."}), 404

    return parse_json(my_month_res), 200




@period_area_blueprint.route('/accidents/area/<area>/week/<week>', methods=['GET'])
def get_accidents_by_area_and_week(area, week):
    week_accidents =  find_the_week(week, area)

    if not week_accidents:
        return jsonify({"message": "No accidents found for this area and date."}), 404

    return parse_json(week_accidents), 200