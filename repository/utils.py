from datetime import timedelta, datetime


# def get_week_range(date):
#     start = date - timedelta (days=date.weekday())
#     end = start + timedelta(days=6)
#     return start.date(), end.date()
#
#
# def parse_date(date_str: str):
#     has_seconds = len(date_str.split(' ')) > 2
#     date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
#     return datetime.strptime(date_str, date_format)
#
#
# def extract_the_month(str_date):
#     date_object = datetime.strptime(str_date, '%m/%d/%Y %H:%M')
#     # Extract the month
#     month = date_object.month
#     return month



import json
from bson import json_util

from database.connect import daily_collection, weekly_collection


def parse_json(data):
    return json.loads(json_util.dumps(data))


def find_the_day(date, area):
    date_object = datetime.strptime(date, '%m-%d-%Y')
    start_of_day = date_object.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)
    query = {
        'area': area,
        'date': {
            '$gte': start_of_day,
            '$lt': end_of_day
        }
    }
    the_query = list(daily_collection.find(query))
    return the_query



def find_the_week(date, area):
    date_object = datetime.strptime(date, '%m-%d-%Y')
    start_of_day = date_object.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)
    query = {
        'area': area,
        'week_start': {
            '$gte': start_of_day,
            '$lt': end_of_day
        }
    }
    the_query = list(weekly_collection.find(query))
    return the_query