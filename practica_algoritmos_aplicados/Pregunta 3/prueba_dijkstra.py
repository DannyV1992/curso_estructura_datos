from dijkstra import Graph

if __name__ == "__main__":
    # Crear un grafo con 8 nodos (A, B, C, D, E, F, G, H)
    g = Graph(8)

    # Representación del grafo como una matriz de adyacencia
    # Los índices corresponden a los nodos en orden: A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7
    g.graph = [
        [0, 3, 5, 0, 0, 0, 0, 10],  # A
        [3, 0, 5, 6, 4, 0, 6, 9],   # B
        [5, 5, 0, 0, 1, 7, 0, 0],   # C
        [0, 6, 0, 0, 12, 0, 3, 2],  # D
        [0, 4, 1, 12, 0, 0, 15, 0], # E
        [0, 0, 7, 0, 0, 0, 0, 0],   # F
        [0, 6, 0, 3, 15, 0, 0, 9],  # G
        [10, 9, 0, 2, 0, 0, 9, 0]   # H
    ]

    # Ejecutar el algoritmo de Dijkstra desde el nodo A (índice = 0)
    g.dijkstra(0)
