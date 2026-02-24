from flask import Flask, session, redirect, request
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from config import Config
from .models import db
from .translations import translate   # 👈 import translator

login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ============================
    # Initialize Extensions
    # ============================
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    # ============================
    # Prevent Cache (important)
    # ============================
    @app.after_request
    def add_header(response):
        response.headers["Cache-Control"] = "no-store"
        return response

    # ============================
    # Language Route
    # ============================
    @app.route("/set_language/<lang>")
    def set_language(lang):
        if lang in ["en", "hi", "te"]:
            session["lang"] = lang
        return redirect(request.referrer or "/")

    # ============================
    # Inject Translator into Templates
    # ============================
    @app.context_processor
    def inject_translator():
        def _(text):
            lang = session.get("lang", "en")
            return translate(text, lang)
        return dict(_=_)

    # ============================
    # Inject Pending Users Count (ADMIN ONLY)
    # ============================
    from .models import User

    @app.context_processor
    def inject_pending_count():
        if current_user.is_authenticated and current_user.role == "Admin":
            pending = User.query.filter_by(approved=False).count()
        else:
            pending = 0
        return dict(pending_count=pending)

    # ============================
    # User Loader
    # ============================
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ============================
    # Register Blueprints
    # ============================
    from .auth import auth
    from .dashboard import dashboard
    from .forecast import forecast
    from .inventory import inventory

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(forecast)
    app.register_blueprint(inventory)

    # ============================
    # Create Database
    # ============================
    with app.app_context():
        db.create_all()

    return app