class nodo:
    # single linked list node
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def setNext(self, next_node):
        self.__next = next_node

    def getNext(self):
        return self.__next

    def __str__(self):
        return f"Data: {self.__data}"