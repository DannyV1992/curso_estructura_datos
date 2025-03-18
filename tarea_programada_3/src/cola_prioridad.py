from nodo import Nodo

class ColaPrioridad:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def insertar(self, persona):
        nuevo_nodo = Nodo(persona)
        if self.__head is None:
            self.__head = nuevo_nodo
        elif persona.get_edad() >= 65:
            if self.__head.getData().get_edad() < 65:
                nuevo_nodo.setNext(self.__head)
                self.__head = nuevo_nodo
            else:
                current = self.__head
                while current.getNext() and current.getNext().getData().get_edad() >= 65:
                    current = current.getNext()
                nuevo_nodo.setNext(current.getNext())
                current.setNext(nuevo_nodo)
        else:
            current = self.__head
            while current.getNext():
                current = current.getNext()
            current.setNext(nuevo_nodo)
        self.__count += 1

    def imprimir(self):
        print(f"Total de personas en la cola: {self.__count}")
        current = self.__head
        while current:
            print(current.getData())
            current = current.getNext()

    def eliminar(self):
        if self.__head is None:
            print("La cola está vacía")
            return None
        persona_eliminada = self.__head.getData()
        self.__head = self.__head.getNext()
        self.__count -= 1
        return persona_eliminada
