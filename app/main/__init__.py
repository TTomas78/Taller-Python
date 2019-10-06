from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .config import config_by_name
from app.main.services.model_charger_service import ModelCharger
db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config.from_object(config_by_name[config_name])
    ModelCharger()

    with app.app_context():
        db.init_app(app)
        return app