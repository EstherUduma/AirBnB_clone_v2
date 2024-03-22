#!/usr/bin/python3
"""Starts a Flask web application with three routes.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays the 'Hello HBNB!'.
    /hbnb: Displays the 'HBNB'.
    /c/<text>: Displays the 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route that displays 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """
    Route that displays 'C' followed by the value of text variable
    """
    # Replace underscores with spaces in the text variable
    text = text.replace("_", " ")
    return "C " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
