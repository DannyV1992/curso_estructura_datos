import pickle
import os
from persona import Persona

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "personas.dat")

personas = [
    Persona("Alice", 25, "123 Street", 1999),
    Persona("Bob", 30, "456 Avenue", 1994),
    Persona("Charlie", 28, "789 Road", 1996),
    Persona("David", 35, "101 Blvd", 1989),
    Persona("Eve", 22, "202 Lane", 2002)
]

# escribiendo los objetos al archivo
with open(filename, "wb") as file:
    for person in personas:
        pickle.dump(person, file)

# los leemos para imprimirlos y guardar las posiciones o indices
posiciones = []
personas_leidas = []
with open(filename, "rb") as file:
    while True:
        try:
            pos = file.tell()  # posicion actual en el archivo
            person = pickle.load(file)
            posiciones.append(pos)
            personas_leidas.append(person)
        except EOFError:
            break

# imprimir personas leidas
print("\nRetrieved objects:")
for person in personas_leidas:
    print(person)

# modificamos la persona en la posicion 1
personas_leidas[1].set_age(121)
personas_leidas[1].set_name("el mas topo")


with open(filename, "r+b") as file:  # abrimos para lectura-escritura
    # podria ser w+b? escribimos en el indice de la posicion
    # y luego actualizamos el resto del archivo correspondientemente
    file.seek(posiciones[1])
    pickle.dump(personas_leidas[1], file)
    for persona in personas_leidas[2:]:
        pickle.dump(persona,file)

# abrimos de nuevo para leer los datos actualizados
personas_actualizadas = []
with open(filename, "rb") as file:
    while True:
        try:
            personas_actualizadas.append(pickle.load(file))
        except EOFError:
            break

print("\ndatos actualizados:")
for person in personas_actualizadas:
    print(person)
