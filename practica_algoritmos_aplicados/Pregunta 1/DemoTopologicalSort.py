from GraphVariant1 import Graph

def main():
    # Grafo 1
    print("\nGrafo 1:")
    g1 = Graph(6)
    g1.addEdge(0, 4)
    g1.addEdge(4, 1)
    g1.addEdge(4, 2)
    g1.addEdge(2, 3)
    g1.addEdge(2, 5)

    print("Ordenamiento topológico del Grafo 1:")
    g1.topologicalSort()

    # Grafo 2
    print("\nGrafo 2:")
    g2 = Graph(5)
    g2.addEdge(0, 1)  # A -> B
    # g2.addEdge(1, 0)  # B -> A
    # g2.addEdge(2, 1)  # C -> B
    g2.addEdge(1, 2)  # B -> C
    g2.addEdge(2, 3)  # C -> D
    # g2.addEdge(3, 2)  # D -> C
    g2.addEdge(3, 0)  # D -> A
    g2.addEdge(4, 0)  # E -> A

    print("Ordenamiento topológico del Grafo 2:")
    g2.topologicalSort()

    # Grafo 3
    print("\nGrafo 3:")
    g3 = Graph(7)
    g3.addEdge(0, 1)  # a -> b
    g3.addEdge(0, 5)  # a -> s
    g3.addEdge(1, 4)  # b -> m
    g3.addEdge(1, 6)  # b -> t
    g3.addEdge(6, 3)  # t -> k
    g3.addEdge(6, 2)  # t -> g
    g3.addEdge(2, 5)  # g -> s

    print("Ordenamiento topológico del Grafo 3:")
    g3.topologicalSort()

if __name__ == "__main__":
    main()
