from Persona import Persona
from persona_comparator import comparator

unaPersona1 = Persona("1",22,"Mario")
otraPersona1 = Persona("1",22,"Mario")
unaPersona2 = Persona("1",22,"Mario")
otraPersona2 = Persona("2",23,"Mario")
unaPersona3 = Persona("1",23,"Maria")
otraPersona3 = Persona("1",23,"Mario")

print(comparator.compare(unaPersona3,otraPersona3)) # -1 ok
print(comparator.compare(otraPersona3,unaPersona3)) # 1
print(comparator.compare(unaPersona2,otraPersona2)) # -1 ok
print(comparator.compare(otraPersona2,unaPersona2)) # 1