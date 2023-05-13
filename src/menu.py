class Menu:
    @staticmethod
    def show():
        return "Choose any option:\n1. Add note \n2. Add card \n3. Show notes \n4. Show cards \n5. Exit\n"

    def get_choice(self):
        choice = input(self.show())
        return choice
