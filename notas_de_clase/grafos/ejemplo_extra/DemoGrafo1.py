from pickle import TRUE
from Grafo import Grafo

def main():
    nuevoGrafo = Grafo()
    esDirigido = input("El grafo es dirigido? (S/N)")
    if esDirigido == "S":
        nuevoGrafo.setDirected(True)
    else:
        nuevoGrafo.setDirected(False)
    cantidadNodos = int(input("Cuantos Nodos tiene el grafo?"))
    nuevoGrafo.setNodeQuantity(cantidadNodos)
    nuevoGrafo.imprimirMatriz()
    agregarOpcion = input("Desea agregar una ruta? (S/N)")
    while (agregarOpcion != "N"):
        nodoInicio = int(input("Digite el nodo de inicio:"))
        nodoFinal = int(input("Digite el nodo de destino:"))
        nuevoGrafo.agregarRuta(nodoInicio, nodoFinal)
        nuevoGrafo.imprimirMatriz()
        agregarOpcion = input("Desea agregar una ruta? (S/N)")
    numNodo = int(input("Para cual nodo quiere ver la lista de adyancencia?"))
    nuevoGrafo.listarNodosAdyacentes(numNodo)
    nuevoGrafo.setMatriz([
        [0,1,0,0,1,0,0,0],
        [1,0,0,0,0,1,0,0],
        [0,0,0,1,0,1,1,0],
        [0,0,1,0,0,0,1,1],
        [1,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,1,0],
        [0,0,1,1,0,1,0,1],
        [0,0,0,1,0,0,1,0]
    ])
    nuevoGrafo.breadthFirstGraph(1)

    #Demo practica
    nuevoGrafo.setMatriz([
        [0,1,1,0,0,1,1],
        [1,0,0,0,1,0,0],
        [1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1],
        [0,1,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,0,0,1,1,1,0]
    ])
    print("+======")
    nuevoGrafo.breadthFirstGraph(6)
    print("+======")

    print("*************")
    nuevoGrafo.deepFirstGraph(1)
    print("************")
    nuevoGrafo.setMatriz([
        [0,1,1,0],
        [0,0,1,0],
        [1,0,0,1],
        [0,0,0,1],
    ])
    nuevoGrafo.deepFirstGraph(2)
    #
    #
    # grafo 1 de la practica
    nuevoGrafo.setMatriz([
        [0,1,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,1,1],
        [0,1,0,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,1]
    ])
    print("++++++")
    nuevoGrafo.deepFirstGraph(0)


if __name__ == "__main__":
    main()