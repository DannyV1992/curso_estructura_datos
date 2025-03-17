class doble_pila:

    def __init__(self, total):
        self.__data = [None] * total
        self.__bottom1 = 0
        self.__top1 = 0
        self.__bottom2 = total // 2
        self.__top2 = total // 2

    def push(self, pila, element):
        if pila == 1:
            self.__data[self.__top1] = element
            self.__top1 = self.__top1 + 1
        elif pila == 2:
            self.__data[self.__top2] = element
            self.__top2 = self.__top2 + 1
    
    def pop(self, pila):
        if pila == 1:
            element = self.__data[self.__top1-1]
            self.__data[self.__top1-1] = None
            self.__top1 = self.__top1 - 1
        elif pila == 2:
            element = self.__data[self.__top2-1]
            self.__data[self.__top2-1] = None
            self.__top2 = self.__top2 - 1
        return element

    def __str__(self):
        mitad_1 = self.__data[:len(self.__data)//2]
        mitad_2 = self.__data[len(self.__data)//2:]
        return f"pila 1: {mitad_1}, pila 2: {mitad_2}"