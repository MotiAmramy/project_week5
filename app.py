from flask import Flask
from repository.csv_repository import init_chicago_car_accidents

app = Flask(__name__)


if __name__ == '__main__':

    init_chicago_car_accidents()
    app.run(debug=True)
