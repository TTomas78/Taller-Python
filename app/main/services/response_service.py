import json
import time


class ResponseService():
    _data: None
    _messages: []
    _success: False

    def init_app(self, app):

        self.reset_service()

        @app.teardown_appcontext
        def teardown_response_service(response_or_exc):
            self.reset_service()
            return response_or_exc

    def reset_service(self):
        self._data = None
        self._messages = []
        self._success = False

    def response(self, data):
        self._data = data
        if self._messages:
            self._success = False
            self._data = None
        else:
            self._success = True
        return self._return_json()

    def add_messages(self, message):
        self._messages.append(message)

    def _return_json(self):
        response = {
            "success": self._success,
            "data": self._data,
            "message": self._messages,
        }
        return response
