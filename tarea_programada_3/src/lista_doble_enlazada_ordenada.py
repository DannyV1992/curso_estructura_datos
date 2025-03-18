from nodo_doble import NodoDoble

class ListaDobleOrdenada:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def insertar(self, persona):
        nuevo_nodo = NodoDoble(persona)
        if self.__head is None:
            self.__head = self.__tail = nuevo_nodo
        elif persona.get_edad() < self.__head.getData().get_edad():
            nuevo_nodo.setNext(self.__head)
            self.__head.setPrev(nuevo_nodo)
            self.__head = nuevo_nodo
        else:
            current = self.__head
            while current.getNext() and current.getNext().getData().get_edad() <= persona.get_edad():
                current = current.getNext()
            nuevo_nodo.setNext(current.getNext())
            nuevo_nodo.setPrev(current)
            if current.getNext():
                current.getNext().setPrev(nuevo_nodo)
            else:
                self.__tail = nuevo_nodo
            current.setNext(nuevo_nodo)
        self.__count += 1

    def imprimir(self):
        print(f"Total de personas en la lista: {self.__count}")
        current = self.__head
        while current:
            print(current.getData())
            current = current.getNext()

    def buscar_por_edad(self, edad):
        if self.__head.getData().get_edad() <= edad <= self.__tail.getData().get_edad():
            diff_head = abs(self.__head.getData().get_edad() - edad)
            diff_tail = abs(self.__tail.getData().get_edad() - edad)
            current = self.__head if diff_head <= diff_tail else self.__tail
            direction = 1 if diff_head <= diff_tail else -1
        else:
            current = self.__head
            direction = 1

        encontrados = []
        while current:
            if current.getData().get_edad() == edad:
                encontrados.append(current.getData())
            elif direction == 1 and current.getData().get_edad() > edad:
                break
            elif direction == -1 and current.getData().get_edad() < edad:
                break
            current = current.getNext() if direction == 1 else current.getPrev()
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
            if self.__head:
                self.__head.setPrev(None)
            else:
                self.__tail = None
        elif posicion == self.__count:
            self.__tail = self.__tail.getPrev()
            self.__tail.setNext(None)
        else:
            current = self.__head
            for _ in range(posicion - 1):
                current = current.getNext()
            current.getPrev().setNext(current.getNext())
            current.getNext().setPrev(current.getPrev())

        self.__count -= 1
        print(f"Elemento en la posición {posicion} ha sido borrado.")
        return True
