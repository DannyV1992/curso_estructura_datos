class Persona:
    def __init__(self, nombre, apellido1, apellido2, edad):
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_apellido1(self):
        return self.__apellido1

    def get_apellido2(self):
        return self.__apellido2

    def get_edad(self):
        return self.__edad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido1(self, apellido1):
        self.__apellido1 = apellido1

    def set_apellido2(self, apellido2):
        self.__apellido2 = apellido2

    def set_edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"Nombre: {self.__nombre} {self.__apellido1} {self.__apellido2}, Edad: {self.__edad}"
