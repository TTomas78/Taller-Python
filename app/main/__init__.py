from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .config import config_by_name
from app.main.services.model_charger_service import ModelCharger
from app.main.services.response_service import ResponseService as ResponseServiceClass

db = SQLAlchemy()
ma = Marshmallow()
ResponseService = ResponseServiceClass()


def create_app(config_name):
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config.from_object(config_by_name[config_name])
    ModelCharger()

    with app.app_context():
        ResponseService.init_app(app)
        db.init_app(app)
        return app