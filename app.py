from datetime import datetime, timedelta

from controllers.accidents_area_controller import accidents_area_blueprint
from controllers.injuries_area_controller import injuries_area_blueprint
from controllers.accidents_cause_controller import accidents_cause_blueprint
# from controllers.accidents_init import
from controllers.period_area_controller import period_area_blueprint
from flask import Flask

from database.connect import daily_collection, weekly_collection
from repository.csv_repository import init_chicago_car_accidents, parse_date

app = Flask(__name__)
app.register_blueprint(accidents_area_blueprint, url_prefix='/api')
app.register_blueprint(injuries_area_blueprint, url_prefix='/api')
app.register_blueprint(accidents_cause_blueprint, url_prefix='/api')
app.register_blueprint(period_area_blueprint, url_prefix='/api')
# app.register_blueprint(accidents_cause_blueprint, url_prefix='/api/cars')

if __name__ == '__main__':
    date_object = datetime.strptime('09-18-2023', '%m-%d-%Y')
    print("Parsed Date:", date_object)

    # Normalize the date to the start of the day
    start_of_day = date_object.replace(hour=0, minute=0, second=0, microsecond=0)
    print("Start of Day:", start_of_day)

    # Calculate the end of the day (start of the next day)
    end_of_day = start_of_day + timedelta(days=1)  # This is the start of the next day

    # Create the query
    query = {
        'area': '411',
        'week_start': {
            '$gte': start_of_day,
            '$lt': end_of_day
        }
    }

    # Perform the query
    a = list(weekly_collection.find(query))
    print(a)


    app.run(debug=True)