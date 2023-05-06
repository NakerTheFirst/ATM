class Keyboard:
    def __init__(self):
        self.__card_id = 0
        self.__card_pin = 1

    @staticmethod
    def take_ui_type():
        """Takes user input for the interface type until the input is correct"""
        ui_type = input("Enter type of interface: console/window\n")
        while not Keyboard.is_ui_correct(ui_type):
            print(f"Input error: input {ui_type} is invalid")
            ui_type = input("Enter type of interface: console/window\n")
        return ui_type

    @staticmethod
    def is_ui_correct(ui_type):
        """Checks if user provided input for interface type is correct"""
        if ui_type == "console" or ui_type == "window":
            return True
        else:
            return False

    def take_card_id(self):
        """Prints prompt and saves user defined card id"""
        self.__card_id = int(input("Enter card id: "))

    def take_card_pin(self):
        """Prints prompt and saves user defined card pin"""
        self.__card_pin = int(input("Enter card pin: "))

    def set_card_pin(self, pin):
        """Sets the card pin"""
        try:
            self.__card_pin = int(pin)
        except ValueError:
            print("User did not provide pin input")

    def set_card_id(self, id):
        """Card id setter"""
        try:
            self.__card_id = int(id)
        except ValueError:
            print("User did not provide id input")

    def get_card_id(self):
        """Card id getter"""
        return self.__card_id

    def get_card_pin(self):
        """Card pin getter"""
        return self.__card_pin
