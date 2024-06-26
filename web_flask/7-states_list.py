#!/usr/bin/python3
"""Flask application"""
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def fetchState():
    """Fetches states from storage"""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def close_session(exception=None):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
