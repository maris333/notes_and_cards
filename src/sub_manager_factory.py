from abc import ABC


class SubManagerFactory(ABC):
    def create_sub_manager(self):
        raise NotImplementedError
