from pila import pila

una_pila = pila(5)

una_pila.push("hola")
print("tope " + str(una_pila.top()))
una_pila.push(5)
print("tope " + str(una_pila.top()))
una_pila.push(3.14)
print("tope " + str(una_pila.top()))

print(una_pila.pop())
print("tope " + str(una_pila.top()))
print(una_pila.pop())
print("tope " + str(una_pila.top()))
una_pila.push("otro dato")
print("tope " + str(una_pila.top()))
print(una_pila.pop())