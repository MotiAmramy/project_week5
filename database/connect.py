from calendar import month

from pymongo import MongoClient


client = MongoClient('mongodb://172.18.105.240:27017')
chicago_car_accidents = client['Chicago_Car_Accidents']
daily_collection = chicago_car_accidents['daily_collection']
weekly_collection = chicago_car_accidents['week_collection']
monthly_collection = chicago_car_accidents['month_collection']
accidents_collection = chicago_car_accidents['accidents_collection']
