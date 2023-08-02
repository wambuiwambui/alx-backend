#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,
    Parametrize templates, Force locale with URL parameter
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ render index.html """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
