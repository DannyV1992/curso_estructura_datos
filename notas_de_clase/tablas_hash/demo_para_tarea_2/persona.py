class Persona:
    def __init__(self, name="", age=0, address="", year=0):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__year = year

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

    def set_year(self, year):
        self.__year = year

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_year(self):
        return self.__year

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, Address: {self.__address}, Year: {self.__year}"