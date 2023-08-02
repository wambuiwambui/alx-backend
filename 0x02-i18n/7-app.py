from flask import Flask, render_template, g, request
from flask_babel import Babel, _
import pytz

app = Flask(__name__)

# Configuring Babel
class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

# Mock user table (same as before)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Get user function (same as before)
def get_user():
    user_id = request.args.get('login_as', type=int)
    if user_id in users:
        return users[user_id]
    return None

# get_timezone function
@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')  # Look for timezone parameter in URL parameters
    if timezone:
        try:
            # Validate if it is a valid timezone using pytz
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    user = get_user()
    if user and user['timezone']:
        try:
            # Validate if it is a valid timezone using pytz
            pytz.timezone(user['timezone'])
            return user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']

# before_request function to set g.user
@app.before_request
def before_request():
    g.user = get_user()
    g.timezone = get_timezone()

# Route and template
@app.route('/')
def index():
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

