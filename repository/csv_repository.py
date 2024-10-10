import csv
from datetime import datetime, timedelta

from database.connect import daily_collection,  monthly_collection,accidents_collection, weekly_collection
import os

# from repository.utils import parse_date, get_week_range, extract_the_month



def get_week_range(date):
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=6)
    return start, end  # Return as datetime objects

def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)

def extract_the_month(str_date):
    date_object = parse_date(str_date)
    return date_object.month

def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row

def safe_int(value, default=0):
    """Convert a string to an integer, returning default if empty or invalid."""
    try:
        return int(value) if value else default
    except ValueError:
        return default

def init_chicago_car_accidents():
    weekly_collection.drop()
    daily_collection.drop()
    monthly_collection.drop()
    accidents_collection.drop()

    for row in read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')):
        crash_record_id = row['CRASH_RECORD_ID']
        if accidents_collection.find_one({'CRASH_RECORD_ID': crash_record_id}):
            continue  # Skip this record if it already exists

        # Parse the crash date
        crash_date = parse_date(row['CRASH_DATE'])

        # Create the accident dictionary
        accident = {
            'CRASH_DATE': crash_date,
            'BEAT_OF_OCCURRENCE': row['BEAT_OF_OCCURRENCE'],
            'injuries': {
                'INJURIES_TOTAL': safe_int(row['INJURIES_TOTAL']),
                'fatal': safe_int(row['INJURIES_FATAL']),
                'non_fatal': safe_int(row['INJURIES_INCAPACITATING']) + safe_int(row['INJURIES_NON_INCAPACITATING'])
            },
            'PRIM_CONTRIBUTORY_CAUSE': row['PRIM_CONTRIBUTORY_CAUSE'],
        }

        # Insert accident into accidents collection
        accidents_collection.insert_one(accident)

        # Create daily, weekly, and monthly entries
        daily = {
            'area': row['BEAT_OF_OCCURRENCE'],
            'date': crash_date,  # Keep as datetime
            'cause': [row['PRIM_CONTRIBUTORY_CAUSE']],
            'total_accidents': 1,
            'injuries': {
                'INJURIES_TOTAL': safe_int(row['INJURIES_TOTAL']),
                'fatal': safe_int(row['INJURIES_FATAL']),
                'non_fatal': safe_int(row['INJURIES_INCAPACITATING']) + safe_int(row['INJURIES_NON_INCAPACITATING']),
            }
        }

        week_start, week_end = get_week_range(crash_date)
        weekly = {
            'area': row['BEAT_OF_OCCURRENCE'],
            'week_start': week_start,
            'week_end': week_end,
            'cause': [row['PRIM_CONTRIBUTORY_CAUSE']],
            'total_accidents': 1,
            'injuries': {
                'INJURIES_TOTAL': safe_int(row['INJURIES_TOTAL']),
                'fatal': safe_int(row['INJURIES_FATAL']),
                'non_fatal': safe_int(row['INJURIES_INCAPACITATING']) + safe_int(row['INJURIES_NON_INCAPACITATING']),
            }
        }

        month = extract_the_month(row['CRASH_DATE'])
        monthly = {
            'area': row['BEAT_OF_OCCURRENCE'],
            'month': month,
            'cause': [row['PRIM_CONTRIBUTORY_CAUSE']],
            'total_accidents': 1,
            'injuries': {
                'INJURIES_TOTAL': safe_int(row['INJURIES_TOTAL']),
                'fatal': safe_int(row['INJURIES_FATAL']),
                'non_fatal': safe_int(row['INJURIES_INCAPACITATING']) + safe_int(row['INJURIES_NON_INCAPACITATING']),
            }
        }

        # Insert into daily collection
        daily_collection.update_many(
            {'area': daily['area'], 'date': daily['date']},
            {'$inc': {'total_accidents': 1, 'injuries.INJURIES_TOTAL': daily['injuries']['INJURIES_TOTAL'],
                       'injuries.fatal': daily['injuries']['fatal'],
                       'injuries.non_fatal': daily['injuries']['non_fatal']}},
            upsert=True
        )

        # Insert into weekly collection
        weekly_collection.update_many(
            {'area': weekly['area'], 'week_start': weekly['week_start'], 'week_end': weekly['week_end']},
            {'$inc': {'total_accidents': 1, 'injuries.INJURIES_TOTAL': weekly['injuries']['INJURIES_TOTAL'],
                       'injuries.fatal': weekly['injuries']['fatal'],
                       'injuries.non_fatal': weekly['injuries']['non_fatal']}},
            upsert=True
        )

        # Insert into monthly collection
        monthly_collection.update_many(
            {'area': monthly['area'], 'month': monthly['month']},
            {'$inc': {'total_accidents': 1, 'injuries.INJURIES_TOTAL': monthly['injuries']['INJURIES_TOTAL'],
                       'injuries.fatal': monthly['injuries']['fatal'],
                       'injuries.non_fatal': monthly['injuries']['non_fatal']}},
            upsert=True
        )