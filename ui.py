import tkinter as tk


class UserInterface:
    @staticmethod
    def create_ui(ui_type):
        if ui_type == "console":
            return ConsoleInterface()
        elif ui_type == "window":
            return WindowInterface()

    def view_menu(self):
        pass

    def print_ver_result(self, is_correct):
        pass


class ConsoleInterface(UserInterface):
    def view_menu(self):
        prompt = "Hello! To withdraw money, please enter card id and pin number, separated by space."
        instr = "The card id is 2 digits long. The pin number is 4 digits long."
        print(prompt + "\n" + instr)

    def print_ver_result(self, is_correct):
        if is_correct:
            message = "Verification successful. \n*ATM withdraws 50 PLN*"
        else:
            message = "Verification unsuccessful. \n*ATM shuts down*"
        print(message)


class WindowInterface(UserInterface):
    def view_menu(self):
        # Root config
        root = tk.Tk()
        root.title("ATM")
        root.geometry("640x720")
        root.configure(bg="#302c2c")
        icon = tk.PhotoImage(file="icon.ico")
        root.iconphoto(False, icon)

        root.mainloop()

    def print_ver_result(self, is_correct):
        pass
