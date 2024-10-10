from datetime import datetime, timedelta

from controllers.accidents_area_controller import accidents_area_blueprint
from controllers.injuries_area_controller import injuries_area_blueprint
from controllers.accidents_cause_controller import accidents_cause_blueprint
from controllers.accidents_init import accidents_init_blueprint
from controllers.period_area_controller import period_area_blueprint
from flask import Flask

from database.connect import daily_collection, weekly_collection, accidents_collection
from repository.csv_repository import init_chicago_car_accidents, parse_date

app = Flask(__name__)
app.register_blueprint(accidents_area_blueprint, url_prefix='/api')
app.register_blueprint(injuries_area_blueprint, url_prefix='/api')
app.register_blueprint(accidents_cause_blueprint, url_prefix='/api')
app.register_blueprint(period_area_blueprint, url_prefix='/api')
app.register_blueprint(accidents_init_blueprint, url_prefix='/api')

if __name__ == '__main__':
    accidents = list(accidents_collection.find({'BEAT_OF_OCCURRENCE': '222'}))
    app.run(debug=True)