from src.notes_sub_manager import NotesSubManager
from src.sub_manager_factory import SubManagerFactory


class NotesSubManagerFactory(SubManagerFactory):
    def create_sub_manager(self):
        return NotesSubManager()
