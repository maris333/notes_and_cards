from abc import ABC


class AbstractSubManager(ABC):
    def add(self, element):
        raise NotImplementedError

    def show(self):
        raise NotImplementedError
