class Cola:

    def __init__(self, size):
        self.__data = []
        for _ in range(0, size):
            self.__data.append(None)
        self.__tail = 0
        self.__head = 0

    def enqueue(self, item):
        self.__data[self.__tail] = item
        self.__tail = self.__tail + 1

    def dequeue(self):
        item = self.__data[self.__head]
        self.__head = self.__head + 1
        return item