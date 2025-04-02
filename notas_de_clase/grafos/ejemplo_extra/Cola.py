class Cola:
    __datos = []

    def isEmpty(self):
        return len(self.__datos) == 0

    def queue(self, elemento):
        self.__datos.append(elemento)
    
    def dequeue(self):
        if not len(self.__datos) == 0:
            return self.__datos.pop(0)
        else:
            return None