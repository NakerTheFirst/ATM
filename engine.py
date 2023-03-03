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

    def verify(self):
        for elem in self.db._tab:
            if elem[0] == self.__id and elem[1] == self.__pin:
                return True
        return False

    def run(self):
        self.screen.print_menu()
        self.__id, self.__pin = self.keyboard.take_input()
        ver_result = self.verify()
        self.screen.print_ver_result(ver_result)
