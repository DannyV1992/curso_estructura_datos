class nueva_cola:

    def __init__(self, max):
        self.__max = max
        self.__data = []

    def enqueue(self, item):
        if len(self.__data) < self.__max:
            self.__data.append(item)
        else:
            raise IndexError("The queue is full")
    
    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        else:
            return None
        
    def is_empty(self):
        return len(self.__data) == 0