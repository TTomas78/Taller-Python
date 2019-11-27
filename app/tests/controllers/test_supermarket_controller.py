from main import app
from flask import current_app
from app.main.controllers.supermarket_controller import SupermarketListResource


class TestSupermarketController(object):

    ctx = app.app_context()
    controller = SupermarketListResource()

    def setup_method(self, method):  # pylint: disable=unused-argument
        self.ctx.push()

    def teardown_method(self, method):  # pylint: disable=unused-argument
        self.ctx.pop()

    def test_supermarket_list_resource(self, monkeypatch):
        with current_app.test_request_context():
            with monkeypatch.context() as monkey: