import importlib


class ModelCharger():
    def __init__(self):
        importlib.import_module('app.main.models')