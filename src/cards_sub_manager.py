from src.abstract_sub_manager import AbstractSubManager


class CardsSubManager(AbstractSubManager):
    def __init__(self):
        super().__init__()
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def show(self):
        print("Cards:")
        for card in self.cards:
            print(card)
