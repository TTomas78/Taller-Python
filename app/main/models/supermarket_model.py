from app.main import db
from app.main.models.base_model import BaseModel
from app.main.utils.seconds_converter import seconds_to_time
from app.main.utils.seconds_converter import time_to_seconds

class SupermarketModel(BaseModel):
    __tablename__ = 'supermarkets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    _open_time = db.Column("open_time", db.Integer(), nullable=False)
    _close_time = db.Column("close_time", db.Integer(), nullable=False)

    @property
    def open_time(self):
        """Return open_time value"""
        return seconds_to_time(self._open_time)

    @open_time.setter
    def open_time(self, value):
        """Set open_time value """
        self._open_time = time_to_seconds(value)

    @property
    def close_time(self):
        """Return close_time value"""
        return seconds_to_time(self._close_time)

    @close_time.setter
    def close_time(self, value):
        """Set close_time value"""
        self._close_time = time_to_seconds(value)
