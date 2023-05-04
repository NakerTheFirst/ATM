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
        pin_pairs = self.db.get_dict()
        if pin_pairs.get(self.__id) == self.__pin:
            return True
        return False

    def _choose_ui(self):
        ui_type = self.keyboard.take_ui_type()
        self.ui = UserInterface.create_ui(ui_type)

    def run(self):
        self._choose_ui()
        # self.ui = UserInterface.create_ui("window")

        if isinstance(self.ui, ConsoleInterface):
            self.ui.view_menu(self.keyboard)
            self.keyboard.take_card_id()
            self.keyboard.take_card_pin()
            self.__id = self.keyboard.get_card_id()
            self.__pin = self.keyboard.get_card_pin()
            self.ui.print_ver_result(self.__is_verified_correctly())

        if isinstance(self.ui, WindowInterface):
            self.ui.view_menu(self.keyboard)
            self.__id = self.keyboard.get_card_id()
            self.__pin = self.keyboard.get_card_pin()
            self.ui.print_ver_result(self.__is_verified_correctly())
