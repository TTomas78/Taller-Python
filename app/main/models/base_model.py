from app.main import db


class CommonModel(db.Model):
    __abstract__ = True


class CommonIsDeletedModel(db.Model):
    __abstract__ = True

    is_deleted = db.Column(db.Boolean(),
                           nullable=False,
                           default=False,
                           server_default='0')


class BaseModel(CommonModel):
    __abstract__ = True

    is_active = db.Column(db.Boolean(),
                          nullable=False,
                          default=True,
                          server_default='1')
    is_deleted = db.Column(db.Boolean(),
                           nullable=False,
                           default=False,
                           server_default='0')
