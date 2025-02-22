from Persona import Persona

class comparator:

    def compare(a: Persona, b: Persona):
        if a.id == b.id and a.nombre == b.nombre and a.edad == b.edad:
            return 0
        elif a.edad < b.edad:
            return -1
        elif a.edad > b.edad:
            return 1
        elif a.edad == b.edad:
            if a.nombre < b.nombre:
                return -1
            elif a.nombre > b.nombre:
                return 1
        else:
            return 0
