#!/usr/bin/env python3
"""Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Babel class config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
app.config.from_object(Config)

@app.route('/')
def index():
    """Render html doc"""
    return render_template('1-index.html')

if __name__ == '__main':
    app.run(debug=True, port = 5001)
