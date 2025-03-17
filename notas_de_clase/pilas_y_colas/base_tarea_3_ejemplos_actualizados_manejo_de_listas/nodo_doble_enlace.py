class nodo_doble:
    # single linked list node
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def setNext(self, next_node):
        self.__next = next_node

    def getNext(self):
        return self.__next

    def setPrev(self, prev_node):
        self.__prev = prev_node

    def getPrev(self):
        return self.__prev
    
    def getData(self):
        return self.__data

    def __str__(self):
        prev = None
        next = None
        if self.__prev != None:
            prev = self.__prev.getData()
        if self.__next != None: 
            next = self.__next.getData()
        return f"Data: {self.__data}, prev = {prev}, next = {next}"