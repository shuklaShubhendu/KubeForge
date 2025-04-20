from flask import Flask
from .db import init_db

from .routes import habit_bp  # ✅ Correct blueprint import

def create_app():
    app = Flask(__name__)
    init_db(app)
    app.register_blueprint(habit_bp)  # ✅ Correct blueprint registered
    return app
