from src.cards_sub_manager_factory import CardsSubManagerFactory
from src.notes_sub_manager_factory import NotesSubManagerFactory


class Executor:
    def __init__(self):
        self.notes_manager = NotesSubManagerFactory().create_sub_manager()
        self.cards_manager = CardsSubManagerFactory().create_sub_manager()

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
