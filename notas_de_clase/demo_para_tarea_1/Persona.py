class Persona:

    def __init__(self, id, edad, nombre):
        self.id = id
        self.edad = edad
        self.nombre = nombre

    def __eq__(self, other):
        return self.id == other.id
    
    def __ne__(self, other):
        return self.id != other.id

class Persona2:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        return self.edad == other.edad
    
    def __gt__(self, other):
        return self.edad > other.edad
    
    def __lt__(self, other):
        return self.edad < other.edad