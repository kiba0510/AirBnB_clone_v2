#!/usr/bin/python3
""" Starts Flask!!! """
from flask import Flask, render_template
from models import storage
from models import State, City

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ Removing SQLAlchemy Session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    states = list()
    cities = list()
    for state, value in state_obj.items():
        states.append(value)
    for city, value in city_obj.items():
        cities.append(value)
    return render_template("8-cities_by_states.html",
                           states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run()
