from database import Database
from keyboard import Keyboard
from ui import UserInterface, ConsoleInterface, WindowInterface


class Engine:
    def __init__(self):
        self.db = Database()
        self.keyboard = Keyboard()
        self.ui = None
        self.__id = None
        self.__pin = None

    def __is_verified_correctly(self):
        """Checks if card id and pin pairs match database data"""
        return self.db.get_dict().get(self.__id) == self.__pin

    def _choose_ui(self):
        """Instantiates user defined interface type, Console or Window"""
        ui_type = self.keyboard.take_ui_type()
        self.ui = UserInterface.create_ui(ui_type)

    def run(self):
        """Runs the programme"""
        self._choose_ui()
        self.ui.view_menu(self.keyboard)

        if isinstance(self.ui, ConsoleInterface):
            self.keyboard.take_card_id()
            self.keyboard.take_card_pin()
            self.__id = self.keyboard.get_card_id()
            self.__pin = self.keyboard.get_card_pin()
            self.ui.print_ver_result(self.__is_verified_correctly())

        if isinstance(self.ui, WindowInterface):
            self.__id = self.keyboard.get_card_id()
            self.__pin = self.keyboard.get_card_pin()
            self.ui.print_ver_result(self.__is_verified_correctly())
