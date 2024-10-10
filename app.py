from controllers.accidents_area_controller import accidents_area_blueprint
from controllers.injuries_area_controller import injuries_area_blueprint
from controllers.accidents_cause_controller import accidents_cause_blueprint
# from controllers.accidents_init import
from controllers.period_area_controller import
from flask import Flask




app = Flask(__name__)
app.register_blueprint(accidents_area_blueprint, url_prefix='/api')
app.register_blueprint(injuries_area_blueprint, url_prefix='/api')
app.register_blueprint(accidents_cause_blueprint, url_prefix='/api')
app.register_blueprint(accidents_cause_blueprint, url_prefix='/api/cars')
# app.register_blueprint(accidents_cause_blueprint, url_prefix='/api/cars')

if __name__ == '__main__':

    app.run(debug=True)