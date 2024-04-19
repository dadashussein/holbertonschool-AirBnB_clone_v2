#!/usr/bin/python3
"""Start flask app"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def fetchContent():
    """Display content from storage"""
    states = storage.all("State").values()
    places = storage.all("Place").values()
    amenities = storage.all("Amenity").values()
    return render_template("100-hbnb.html",  states=states,
                           places=places, amenities=amenities)


@app.teardown_appcontext
def closeSession(exc):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
