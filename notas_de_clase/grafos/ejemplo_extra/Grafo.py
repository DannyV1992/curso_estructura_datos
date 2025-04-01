from Cola import Cola

class Grafo:
    __matriz = []
    __isDirected = False

    def isDirected(self):
        return self.__isDirected

    def setDirected(self, directed: bool):
        self.__isDirected = directed

    def setMatriz(self, matriz):
        self.__matriz = matriz

    def setNodeQuantity(self, nodeQty: int):
        for cantidad in range(nodeQty):
            nuevaLinea = []
            for cantidad in range(nodeQty):
                nuevaLinea.append(0)
            self.__matriz.append(nuevaLinea)

    def imprimirMatriz(self):
        for linea in self.__matriz:
            for arista in linea:
                print(arista, end = " ")
            print("")

    def agregarRuta(self, inicio, final):
        self.__matriz[inicio][final] = 1
        if self.__isDirected == False:
            self.__matriz[final][inicio] = 1

    def listarNodosAdyacentes(self, nodo):
        listaAdyacencias = self.__matriz[nodo]
        for posicion, columna in enumerate(listaAdyacencias):
            if columna == 1:
                print(f"es adyacente a al nodo #{posicion}")

    def breadthFirstGraph(self, inicio):
        cola = Cola()
        procesados = []
        listaNivel = []
        for nodo in self.__matriz:
            listaNivel.append(len(self.__matriz)+1000)
            procesados.append(0)
        listaNivel[inicio] = 0
        procesados[inicio] = 1
        cola.queue(inicio)
        while not cola.isEmpty():
            nodoEnProceso = cola.dequeue()
            listaAdyacenciaNodoEnProceso = self.__matriz[nodoEnProceso]
            pos = 0
            for nodoAdyacente in listaAdyacenciaNodoEnProceso:
                if nodoAdyacente == 1 and procesados[pos] == 0:
                    procesados[pos] = 1
                    listaNivel[pos] = listaNivel[nodoEnProceso]+1
                    cola.queue(pos)
                pos = pos + 1
            procesados[nodoEnProceso] = 2
        print(listaNivel)


    def deepFirstGraph(self, inicio):
        visited = set()
        self.DFSUtil(inicio, visited)

    def DFSUtil(self, inicio, visited):
        visited.add(inicio)
        listaAdyacencia = self.__matriz[inicio]
        print(f"{inicio}", end= ' ')
        pos = 0
        for nodo in listaAdyacencia:
            if (nodo == 1 and pos not in visited):
                self.DFSUtil(pos, visited)
            pos = pos + 1