class pila:

    def __init__(self, max):
        self.__max = max
        self.__data = []
        for _ in range(0,max):
            self.__data.append(None)
        self.__top = 0

    def is_empty(self):
        return self.__top == 0
    
    def push(self, item):
        if self.__top < self.__max:
            self.__data[self.__top + 1] = item
            self.__top = self.__top + 1
        else:
            raise IndexError("Stack Overflow")
        
    def pop(self):
        if self.__top >= 0:
            data = self.__data[self.__top]
            self.__top = self.__top - 1
            return data
        else:
            raise IndexError("Stack Underflow")
        
    def top(self):
        return self.__data[self.__top]