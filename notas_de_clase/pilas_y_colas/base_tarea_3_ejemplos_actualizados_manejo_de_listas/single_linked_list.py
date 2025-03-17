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

    def delete(self, value):
        if self.__list is None:  # lista vacia?
            print("Nada que borrar")
            return

        # si el dato esta en la cabeza .. .puede re-escribirlo?
        if self.__list.__str__() == f"Data: {value}":
            self.__list = self.__list.getNext()
            return

        # buscamos el dato
        prev = None
        current = self.__list
        while current is not None and current.__str__() != f"Data: {value}":
            prev = current
            current = current.getNext()

        # si siempre no esta el dato
        if current is None:
            print(f"Node with value {value} not found.")
            return

        # aqui "bricamos el dato si lo encontramos".
        #ojo solo borramos la primera ocurrencia
        prev.setNext(current.getNext())

    def imprimir(self):
        current = self.__list
        print(current)
        if current != None:
            while current.getNext() != None:
                current = current.getNext()
                print(current)