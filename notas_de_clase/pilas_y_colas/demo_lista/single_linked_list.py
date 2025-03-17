from nodo import nodo

class single_linked_list:

    def __init__(self):
        self.__list = None

    def insert(self, nodo):
        if self.__list == None:
            self.__list = nodo
        else:
            current = self.__list
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(nodo)
    
    def imprimir(self):
        current = self.__list
        print(current)
        if current != None:
            while current.getNext() != None:
                current = current.getNext()
                print(current)