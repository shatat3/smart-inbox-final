from flask import Flask
from flask_dance.contrib.google import make_google_blueprint
from config import SECRET_KEY, GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    google_bp = make_google_blueprint(
        client_id=GOOGLE_OAUTH_CLIENT_ID,
        client_secret=GOOGLE_OAUTH_CLIENT_SECRET,
        redirect_to="home",
        scope=["profile", "email"]
    )

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(google_bp, url_prefix="/login")

    return app
