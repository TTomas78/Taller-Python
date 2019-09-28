import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app import blueprint


app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

@app.cli.command
def run():
    app.run(debug=True)

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback() # pylint: disable=no-member
    db.session.remove()