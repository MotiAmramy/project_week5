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


def parse_json(data):
    return json.loads(json_util.dumps(data))