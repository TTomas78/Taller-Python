class ResourceAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Entity already exists'