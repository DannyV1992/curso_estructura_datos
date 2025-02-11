import random
from datetime import datetime

def main():
    lista = crearLista()
    preguntarPorNumeros(lista)

def crearLista():
    nuevaLista = []
    cantidadDatos = int(input("Cuantos elementos quiere meter?")) 
    for nuevoElemento in range(cantidadDatos):
        nuevaLista.append(random.randint(0,100000))
    nuevaLista.sort()
    print(nuevaLista)
    return nuevaLista

def preguntarPorNumeros(listaDatos):
    opcion = 0
    while (opcion != 2):
        numeroABuscar = int(input("Cual numero quiere buscar?"))
        if (busquedaBinaria(listaDatos, numeroABuscar)):
            print("El numero esta!")
        else:
            print("El numero NO esta!")
        opcion = int(input("Quiere preguntar otro numero? (Oprima cualquier numero o 2 para terminar)"))

def busquedaBinaria(arreglo, numero):
    comparaciones = 0
    print(datetime.now())
    limIzq = 0
    limDer = len(arreglo)-1

    while limIzq <= limDer:
        comparaciones = comparaciones + 1 
        mitad = (limDer + limIzq) // 2
        if arreglo[mitad] < numero:
            limIzq = mitad + 1
        elif arreglo[mitad] > numero: 
            limDer = mitad -1
        else: 
            print(f"Hizo {comparaciones} comparaciones")
            print(datetime.now())
            return True
    print(f"Hizo {comparaciones} comparaciones")            
    print(datetime.now())
    return False
    
    


if __name__ == "__main__":
    main()