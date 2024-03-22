#!/usr/bin/python3
"""
This script starts a Flask web application with routes for
handling different requests.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Route that displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """Route that displays 'C ' followed by the value of the text variable"""
    # Replace underscores with spaces in the text variable
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text):
    """Displays 'Python ' followed by the value of the text variable"""
    # Replace underscores with spaces in the text variable
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Route that displays 'n is a number' only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """Route that displays an HTML page only if n is an integer"""
    # Render the HTML template with the provided number
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
