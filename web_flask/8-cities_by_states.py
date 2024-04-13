#!/usr/bin/python3
"""Start flask app"""
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route("/cities_by_states")
def fetchCity():
    """Fetch city from storage"""
    states = storage.all("State")
    sorted_state = sorted(states.values(), key=lambda s: s.name)
    return render_template("8-cities_by_states.html", states=sorted_state)


@app.teardown_appcontext
def close_session(ex=None):
    """Close session"""
    storage.close()


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000)
