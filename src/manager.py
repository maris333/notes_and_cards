from src.executor import Executor
from src.menu import Menu


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.executor = Executor()
        self.options = {1: self.executor.add_note, 2: self.executor.add_card, 3: self.executor.show_notes,
                        4: self.executor.show_cards, 5: self.executor.finish}

    def start(self):
        while True:
            try:
                choice = int(self.menu.get_choice())
            except ValueError:
                self._show_error()
            else:
                self._execute(choice)

    @staticmethod
    def _show_error():
        print("Error!")

    def _execute(self, choice):
        self.options.get(choice, self._show_error)()
