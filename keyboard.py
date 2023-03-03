class Keyboard:
    def __init__(self):
        pass

    @staticmethod
    def take_input():
        user_input = input()
        card_id, card_pin = user_input.split()
        card_id = int(card_id)
        card_pin = int(card_pin)
        return card_id, card_pin
