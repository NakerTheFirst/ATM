class Keyboard:
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

    @staticmethod
    def _take_card_id():
        card_id = int(input("Enter card id: "))
        return card_id

    @staticmethod
    def _take_card_pin():
        card_pin = int(input("Enter card pin: "))
        return card_pin
