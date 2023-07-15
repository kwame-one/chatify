from abc import abstractmethod

from app.exceptions.resource_not_found_exception import ResourceNotFoundException


class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def find_all(self, query=None):
        return self.repository.find_all(query)

    def find(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')
        return self.get_dto().model_validate(resource).dict()

    def update(self, id, data):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')
        return self.get_dto().model_validate(self.repository.update(id, data))

    def store(self, data):
        resource = self.repository.store(data)
        print(resource)
        return self.get_dto().model_validate(resource)

    def delete(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Resource not found')
        self.repository.delete(id)
        return True

    @abstractmethod
    def get_dto(self):
        pass
