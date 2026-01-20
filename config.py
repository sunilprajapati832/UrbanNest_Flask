import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload limits (security)
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

    # Session security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Enable only in production (Render/Railway/VPS)
    SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV') == 'production'
