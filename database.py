class Database:
    def __init__(self):
        self.__id_pin_pairs = {11: 1111, 22: 2222, 33: 3333, 44: 4444}

    def get_dict(self):
        """Id-pin pair getter"""
        return self.__id_pin_pairs
