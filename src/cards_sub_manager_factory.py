from src.cards_sub_manager import CardsSubManager
from src.sub_manager_factory import SubManagerFactory


class CardsSubManagerFactory(SubManagerFactory):
    def create_sub_manager(self):
        return CardsSubManager()
