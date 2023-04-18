class Keyboard:
    def __init__(self):
        self.__card_id = None
        self.__card_pin = None

    @staticmethod
    def take_ui_type():
        ui_type = input("Enter type of interface: console/window\n")
        while not Keyboard.is_ui_correct(ui_type):
            print(f"Input error: input {ui_type} is invalid")
            ui_type = input("Enter type of interface: console/window\n")
        return ui_type

    @staticmethod
    def is_ui_correct(ui_type):
        if ui_type == "console" or ui_type == "window":
            return True
        else:
            return False

    def take_card_id(self):
        self.__card_id = int(input("Enter card id: "))

    def take_card_pin(self):
        self.__card_pin = int(input("Enter card pin: "))

    def get_card_id(self):
        return self.__card_id

    def get_card_pin(self):
        return self.__card_pin
