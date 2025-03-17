from nodo import Nodo
from persona import Persona

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def insertar(self, persona):
        nuevo_nodo = Nodo(persona)
        if self.__head is None or persona.get_edad() < self.__head.getData().get_edad():
            nuevo_nodo.setNext(self.__head)
            self.__head = nuevo_nodo
        else:
            current = self.__head
            while current.getNext() and current.getNext().getData().get_edad() <= persona.get_edad():
                current = current.getNext()
            nuevo_nodo.setNext(current.getNext())
            current.setNext(nuevo_nodo)
        self.__count += 1

    def imprimir(self):
        print(f"Total de personas en la lista: {self.__count}")
        current = self.__head
        while current:
            print(current.getData())
            current = current.getNext()

    def buscar_por_edad(self, edad):
        current = self.__head
        encontrados = []
        while current:
            if current.getData().get_edad() == edad:
                encontrados.append(current.getData())
            current = current.getNext()
        return encontrados

    def buscar_por_nombre(self, nombre):
        current = self.__head
        encontrados = []
        while current:
            if nombre.lower() in current.getData().get_nombre().lower():
                encontrados.append(current.getData())
            current = current.getNext()
        return encontrados

    def buscar_por_apellido(self, apellido):
        current = self.__head
        encontrados = []
        while current:
            if (apellido.lower() in current.getData().get_apellido1().lower() or
                apellido.lower() in current.getData().get_apellido2().lower()):
                encontrados.append(current.getData())
            current = current.getNext()
        return encontrados

    def borrar(self, posicion):
        if posicion < 1 or posicion > self.__count:
            print(f"La lista tiene {self.__count} elementos.")
            return False
        if posicion == 1:
            self.__head = self.__head.getNext()
        else:
            current = self.__head
            for _ in range(posicion - 2):
                current = current.getNext()
            current.setNext(current.getNext().getNext())
        self.__count -= 1
        print(f"Elemento en la posición {posicion} ha sido borrado.")
        return True
