from src.abstract_sub_manager import AbstractSubManager


class NotesSubManager(AbstractSubManager):
    def __init__(self):
        super().__init__()
        self.notes = []

    def add(self, note):
        self.notes.append(note)

    def show(self):
        print("Notes:")
        for note in self.notes:
            print(note)
