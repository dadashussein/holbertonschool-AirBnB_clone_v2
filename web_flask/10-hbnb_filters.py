#!/usr/bin/python3
"""Start flask app"""
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def fetchContent():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    sorted_state = sorted(states, key=lambda s: s.name)
    return render_template("6-index.html", states=sorted_state,
                           amenities=amenities)


@app.teardown_appcontext
def closeSession(exception):
    """Close session"""
    storage.close()


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000)
