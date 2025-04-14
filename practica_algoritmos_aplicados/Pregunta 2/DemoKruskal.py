from GraphKruskal import Graph

def main():
    # Solución para el primer grafo (6 nodos: a=1, b=2, c=3, d=4, e=5, f=6)
    print("Solución para el primer grafo:")
    g1 = Graph(6)  # 6 vértices

    # Agregando las aristas con sus pesos calculados
    g1.addEdge(0, 1, 3)  # a-b
    g1.addEdge(0, 2, 4)  # a-c
    g1.addEdge(0, 5, 7)  # a-f
    g1.addEdge(1, 2, 5)  # b-c
    g1.addEdge(1, 5, 8)  # b-f
    g1.addEdge(2, 3, 7)  # c-d
    g1.addEdge(2, 4, 8)  # c-e
    g1.addEdge(3, 4, 9)  # d-e
    g1.addEdge(4, 5, 11) # e-f

    # Llamada a la función KruskalMST
    g1.KruskalMST()

    print("\nSolución para el segundo grafo:")
    # Solución para el segundo grafo (4 nodos: a=1, b=2, c=3, d=4)
    g2 = Graph(4)  # 4 vértices

    # Agregando las aristas con sus pesos calculados
    g2.addEdge(0, 1, 3)  # a-b
    g2.addEdge(0, 2, 4)  # a-c
    g2.addEdge(1, 2, 5)  # b-c
    g2.addEdge(1, 3, 6)  # b-d
    g2.addEdge(2, 3, 7)  # c-d

    # Llamada a la función KruskalMST
    g2.KruskalMST()

if __name__ == "__main__":
    main()


