import json
import time


class ResponseService():
    def __init__(self):
        self._data = None
        self._messages = []
        self._success = False

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
