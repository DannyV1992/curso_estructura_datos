#Representa un grafo no dirigido por una matriz de adyacencia
class grafo_matriz:
    def __init__(self, node_qty):
        self.__matriz = []
        for _ in range(0,node_qty):
            self.__matriz.append([0] * node_qty)
    
    def show_graph_matriz(self):
        for row in self.__matriz:
            print(row)
    
    def add_edge(self, src, dst):
        self.__matriz[src][dst] = 1
        self.__matriz[dst][src] = 1

    def list_adyacency(self, node):
        adyacency_list = []
        for col in range(0, len(self.__matriz)):
            if self.__matriz[node][col] == 1:
                adyacency_list.append(col)
        return adyacency_list