class ResourceNotFoundException(Exception):
    def __init__(self, entity_id):
        self.message = 'Entity {} not found'.format(entity_id)