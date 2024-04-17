#!/usr/bin/python3
"""Start flask app"""
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def fetchState():
    """Fetch state"""
    return render_template("9-states.html", states=storage.all("State"))


@app.route("/states/<id>", strict_slashes=False)
def fetchCityWithID(id):
    """Fetch city with id"""
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000)
