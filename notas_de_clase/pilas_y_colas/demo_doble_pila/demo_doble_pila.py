from doble_pila import doble_pila

una_doble_pila = doble_pila(10)
una_doble_pila.push(1,"hola")
una_doble_pila.push(1,33)
una_doble_pila.push(1,"adios")
una_doble_pila.push(2,"hola")
una_doble_pila.push(2,"adios")
print(una_doble_pila)
una_doble_pila.pop(1)
una_doble_pila.pop(2)
print(una_doble_pila)