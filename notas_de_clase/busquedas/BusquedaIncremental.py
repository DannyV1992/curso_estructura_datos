from operator import truediv
import random
from datetime import datetime

def main():
    listaDatos = crearLista()
    preguntarPorNumeros(listaDatos)

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
        if (encuentraNumero(listaDatos, numeroABuscar)):
            print("El numero esta!")
        else:
            print("El numero NO esta!")
        opcion = int(input("Quiere preguntar otro numero? (Oprima cualquier numero o 2 para terminar)"))

def encuentraNumero(lista, numero):
    print(datetime.now())
    indice = 0
    valorActual = lista[indice]
    comparaciones = 0
    while valorActual <= numero:
        comparaciones = comparaciones + 1
        if valorActual == numero: 
            print(datetime.now())
            print(f"hizo {comparaciones} comparaciones")
            return True
        else:
            indice = indice + 25
            if indice >= len(lista):
                indice = len(lista)-1
            valorActual = lista[indice]
    #aqui o lo encontre o llegue al final
    indiceMinimo = indice -25
    while indice > indiceMinimo or lista[indice] > numero:
        valorActual = lista[indice]
        comparaciones = comparaciones + 1
        if valorActual == numero:
            print(datetime.now())
            print(f"hizo {comparaciones} comparaciones")
            return True
        indice = indice -1             
    print(datetime.now())
    print(f"hizo {comparaciones} comparaciones")
    return False

if __name__ == "__main__":
    main()