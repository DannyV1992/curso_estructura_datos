class Tabla_Hash:

    def __init__(self, max):
        self.__table = []
        self.__max = max
        for _ in range(max):
            self.__table.append(None)

    def display_table(self):
        for item in self.__table:
            print(item)
    
    def insert(self, key, item):
        if key > self.__max:
            raise IndexError("key is out of index")
        self.__table[key] = item

    def delete(self, key):
        self.__table[key] = None