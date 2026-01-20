import os
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # ================= EXTENSIONS =================
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # ================= BLUEPRINTS =================
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.property import property_bp
    from app.routes.profile import profile_bp

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(property_bp)
    app.register_blueprint(profile_bp)

    # ================= GLOBAL TEMPLATE CONTEXT =================
    @app.context_processor
    def inject_year():
        return {'current_year': datetime.utcnow().year}

    # ================= ERROR HANDLERS (PHASE 5.3) =================
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.html"), 500

    # ================= SECURITY HEADERS (PHASE 5.4) =================
    @app.after_request
    def add_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response

    # ================= CREATE DB & FOLDERS =================
    with app.app_context():
        from app import models
        db.create_all()

        # Ensure upload directories exist
        static_folder = os.path.join(app.root_path, 'static')
        os.makedirs(os.path.join(static_folder, 'profile_pics'), exist_ok=True)
        os.makedirs(os.path.join(static_folder, 'uploads'), exist_ok=True)

    return app
