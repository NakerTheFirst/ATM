from database import Database
from keyboard import Keyboard
from ui import UserInterface


class Engine:
    def __init__(self):
        self.db = Database()
        self.keyboard = Keyboard()
        self.ui = None
        self.__id = None
        self.__pin = None

    def __verify(self):
        for elem in self.db._tab:
            if elem[0] == self.__id and elem[1] == self.__pin:
                return True
        return False

    def _choose_ui(self):
        ui_type = self.keyboard.take_ui_type()
        self.ui = UserInterface.create_ui(ui_type)

    def run(self):
        self._choose_ui()
        self.ui.view_menu()
        self.__id = self.keyboard._take_card_id()
        self.__pin = self.keyboard._take_card_pin()
        self.ui.print_ver_result(self.__verify())
