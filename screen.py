class Screen:
    def __init__(self):
        pass

    @staticmethod
    def print_menu():
        prompt = "Hello! To withdraw money, please enter card id and pin number, separated by space."
        instr = "The card id is 2 digits long. The pin number is 4 digits long."
        print(prompt + "\n" + instr)

    @staticmethod
    def print_ver_result(is_correct):
        if is_correct:
            message = "Verification successful. \n*ATM withdraws 50 PLN*"
        else:
            message = "Verification unsuccessful. \n*ATM shuts down*"
        print(message)
