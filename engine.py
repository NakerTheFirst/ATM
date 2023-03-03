from database import Database
from screen import Screen
from keyboard import Keyboard


class Engine:
    def __init__(self):
        self.db = Database()
        self.screen = Screen()
        self.keyboard = Keyboard()
        self.__id = None
        self.__pin = None

    def __verify(self):
        for elem in self.db._tab:
            if elem[0] == self.__id and elem[1] == self.__pin:
                return True
        return False

    def _run(self):
        self.screen._print_menu()
        self.__id, self.__pin = self.keyboard._take_input()
        ver_result = self.__verify()
        self.screen._print_ver_result(ver_result)
