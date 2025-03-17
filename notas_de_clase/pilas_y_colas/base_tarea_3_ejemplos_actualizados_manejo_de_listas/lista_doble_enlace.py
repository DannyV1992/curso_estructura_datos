from nodo_doble_enlace import nodo_doble

class lista_doble_enlace:
#lista doblemente enlazada que 
#SIEMPRE inserta al final

    def __init__(self):
        self.__list = None

    def insert(self, new_node):

        # si la lista esta vacia... es la nueva cabeza
        if self.__list is None:
            self.__list = new_node
            return

        # si no, vaya al ultimo nodo
        current = self.__list
        while current.getNext():
            current = current.getNext()

        # agregue el nuevo nodo al final.
        current.setNext(new_node)
        new_node.setPrev(current)

    def imprimir(self):
        current = self.__list
        print(current)
        if current != None:
            while current.getNext() != None:
                current = current.getNext()
                print(current)

    def delete(self, item):
        current = self.__list
        while current: #recorremos la lista para encontrar match
            if current.getData() == item:
                # si es la cabeza
                if current.getPrev() is None:
                    self.__list = current.getNext()
                    if self.__list:  #actualizamos el prev de la nueva cabeza
                        self.__list.setPrev(None)

                # si es el ultimo nodo
                elif current.getNext() is None:
                    current.getPrev().setNext(None)

                # no es la cabeza ni la cola 
                else:
                    current.getPrev().setNext(current.getNext())
                    current.getNext().setPrev(current.getPrev())

                del current  # NOVEDAD!! esto libera memoria
