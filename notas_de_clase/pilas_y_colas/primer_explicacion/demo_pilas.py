from pila import Pila

una_pila = Pila(5)

una_pila.push("Hola")
una_pila.push(5)
una_pila.push(3.14)

print(una_pila.pop())
print(una_pila.pop())
una_pila.push("Otro dato")
print(una_pila.pop())
print(una_pila.pop())
print(una_pila.pop())
print(una_pila.pop())