class ResourceNotFoundException(Exception):
    def __init__(self, entity_id):
        self.messages = 'Entity {} not found'.format(entity_id)