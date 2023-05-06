import tkinter as tk


class UserInterface:
    @staticmethod
    def create_ui(ui_type):
        """Returns either ConsoleInterface or WindowInterface object"""
        if ui_type == "console":
            return ConsoleInterface()
        elif ui_type == "window":
            return WindowInterface()

    def view_menu(self, keyboard):
        pass

    def print_ver_result(self, is_correct):
        pass


class ConsoleInterface(UserInterface):
    def view_menu(self, keyboard):
        """Prints the console menu"""
        prompt = "Hello! To withdraw money, please enter card id and then pin number, separated with enter."
        instr = "The card id is 2 digits long. The pin number is 4 digits long."
        print(prompt + "\n" + instr)

    def print_ver_result(self, is_correct):
        """Prints the result of user input - database data verification"""
        if is_correct:
            message = "Verification successful. \n*ATM withdraws 50 PLN*"
        else:
            message = "Verification unsuccessful. \n*ATM shuts down*"
        print(message)


class WindowInterface(UserInterface):
    def view_menu(self, keyboard):
        """Renders GUI"""
        # Root config
        root = tk.Tk()
        root.title("ATM")
        root.geometry("640x720")
        root.configure(bg="#39393A")
        icon = tk.PhotoImage(file="icon.ico")
        root.iconphoto(False, icon)

        frame = tk.Frame(master=root, bg="#39393A", width=340, height=480)
        frame.pack(pady=120, padx=200, expand=True, fill="both")

        # Image
        bank_image = tk.PhotoImage(master=frame, file="bank_image.png", width=240, height=160)
        label = tk.Label(master=frame, bg="#39393A", image=bank_image, borderwidth=0, highlightthickness=0)
        label.pack()

        id_var = tk.StringVar()
        pin_var = tk.StringVar()

        # Buttons
        submit_button = tk.Button(frame, text="Submit", command=lambda: self.submit(keyboard, id_var, pin_var, root),
                                  bg="#FF8552", fg="#000", border=0, padx=60, pady=10, activeforeground="#000",
                                  activebackground="#FF8552")
        submit_button.pack(side="bottom", pady=10)

        # ID input box
        id_box = tk.Entry(master=frame, width=30, font=("x", 10), justify="center", bg="#E6E6E6", textvariable=id_var)
        id_var.set("Enter card ID")
        id_box.bind("<FocusIn>", lambda event: id_box.delete('0', 'end'))
        id_box.pack(pady=(80, 20))

        # PIN input box
        pin_box = tk.Entry(master=frame, width=30, font=("x", 10), justify="center", bg="#E6E6E6", textvariable=pin_var)
        pin_var.set("Enter card PIN")
        pin_box.bind("<FocusIn>", lambda event: pin_box.delete('0', 'end'))
        pin_box.pack()

        root.mainloop()

    def print_ver_result(self, is_correct):
        """Renders popup window with the result of user input - database data verification"""
        root = tk.Tk()
        root.title("Verification Result")
        root.geometry("300x150")
        root.configure(bg="#39393A")
        icon = tk.PhotoImage(file="icon.ico")
        root.iconphoto(False, icon)

        if is_correct:
            message = "Verification successful. \n*ATM withdraws 50 PLN*"
        else:
            message = "Verification unsuccessful. \n*ATM shuts down*"

        message_label = tk.Label(master=root, text=message, bg="#39393A", fg="#FFF")
        message_label.pack(pady=10)

        ok_button = tk.Button(root, text="Quit", command=root.destroy, bg="#FF8552", fg="#000",
                              border=0, padx=60, pady=10, activeforeground="#000", activebackground="#FF8552")
        ok_button.pack(pady=10)

        root.mainloop()

    @staticmethod
    def submit(keyboard, id, pin, root):
        """Saves user defined id and pin as Keyboard private attributes and turns off the GUI"""
        id_input = id.get()
        pin_input = pin.get()
        keyboard.set_card_id(id_input)
        keyboard.set_card_pin(pin_input)
        root.destroy()
