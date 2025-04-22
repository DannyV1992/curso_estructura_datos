from grafo_matriz import grafo_matriz

# Grafo 1
mi_grafo = grafo_matriz(7, False)  # El segundo parámetro indica que es NO dirigido

# Agrega las aristas según la imagen
mi_grafo.add_edge(0, 1)
mi_grafo.add_edge(0, 2)
mi_grafo.add_edge(0, 5)
mi_grafo.add_edge(0, 6)
mi_grafo.add_edge(1, 4)
mi_grafo.add_edge(4, 6)
mi_grafo.add_edge(6, 3)
mi_grafo.add_edge(6, 5)
print ("--------GRAFO 1--------")
# Mostrar la matriz de adyacencia
mi_grafo.show_graph_matriz()

# Grafo 2

# El grafo tiene 8 nodos (0 a 7), dirigido
mi_grafo = grafo_matriz(8, True)  # True indica que es dirigido

# Agrega las aristas dirigidas según la imagen
mi_grafo.add_edge(1, 0)
mi_grafo.add_edge(2, 0)
mi_grafo.add_edge(2, 4)
mi_grafo.add_edge(3, 0)
mi_grafo.add_edge(4, 7)
mi_grafo.add_edge(5, 2)
mi_grafo.add_edge(6, 3)
print(" ")
print ("--------GRAFO 2--------")
# Mostrar la matriz de adyacencia
mi_grafo.show_graph_matriz()

# Grafo 3
mi_grafo = grafo_matriz(5, True)  # True indica que es dirigido

# Agrega las aristas dirigidas con sus pesos
mi_grafo.add_edge(0, 1)   # De 0 a 1 con peso 2
mi_grafo.add_edge(0, 2)   # De 0 a 2 con peso 1
mi_grafo.add_edge(0, 4)  # De 0 a 4 con peso 14
mi_grafo.add_edge(1, 2)   # De 1 a 2 con peso 3
mi_grafo.add_edge(1, 3)  # De 1 a 3 con peso 20
mi_grafo.add_edge(1, 4)  # De 1 a 4 con peso 13
mi_grafo.add_edge(2, 4)   # De 2 a 4 con peso 8
mi_grafo.add_edge(4, 3)   # De 4 a 3 con peso 2
print(" ")
print ("--------GRAFO 3--------")
# Mostrar la matriz de adyacencia
mi_grafo.show_graph_matriz()

