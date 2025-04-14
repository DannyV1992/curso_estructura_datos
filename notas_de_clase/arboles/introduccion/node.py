class Nodo:

    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__value = value

    def get_value(self):
        return self.__value

    def insert(self, newNode):
        if self.__value > newNode.get_value():
            if self.__left == None:
                self.__left = newNode
            else:
                self.__left.insert(newNode)
        else:
            if self.__right == None:
                self.__right = newNode
            else: 
                self.__right.insert(newNode)

    def print_preorden(self):
        print(self.__value, end=" ")
        if self.__left != None:
            self.__left.print_preorden()
        if self.__right != None: 
            self.__right.print_preorden()

    def print_inorden(self):
        if self.__left != None:
            self.__left.print_preorden()
        print(self.__value, end=" ")
        if self.__right != None: 
            self.__right.print_preorden()

    def print_postorden(self):
        if self.__left != None:
            self.__left.print_preorden()
        if self.__right != None: 
            self.__right.print_preorden()
        print(self.__value, end=" ")