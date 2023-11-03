from src.cards_sub_manager import CardsSubManager
from src.notes_sub_manager import NotesSubManager


class Executor:
    def __init__(self):
        self.notes_manager = NotesSubManager()
        self.cards_manager = CardsSubManager()

    def add_note(self):
        note = input("Add note: ")
        self.notes_manager.add(note)

    def add_card(self):
        card = input("Add card: ")
        self.cards_manager.add(card)

    def show_notes(self):
        self.notes_manager.show()

    def show_cards(self):
        self.cards_manager.show()

    @staticmethod
    def finish():
        print("Program finished.")
        exit()
