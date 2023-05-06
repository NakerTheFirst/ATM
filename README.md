# ATM
A Python-based ATM simulation created with OOP. The goal is to retrieve user input, verify it with a database, and based on the verification result, either dispense money or shut down. Works in console interface or GUI mode.

## Structure
The programme consists of 6 classes: Engine, Keyboard, UserInterface, ConsoleInterface, WindowInterface, and Database. The UserInterface class is a template for the WindowInterface and ConsoleInterface classes which inherit from it, and use polymorphism to implement their own versions of its methods after compilation. The Database class stores predefined pairs of IDs and PINs, while the Keyboard class provides methods for user input retrieval. The Engine class contains objects of the Database, Keyboard, and ConsoleInterface or WindowInterface classes, and has 3 methods for verifying the ID and PIN, selecting the interface type, and running the program.

## Class scheme
![Class scheme of an ATM simulation](https://github.com/NakerTheFirst/ATM/blob/main/scheme.png)
