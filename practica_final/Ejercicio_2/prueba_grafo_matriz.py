from grafo_matriz import grafo_matriz

graph = grafo_matriz(7, False)  # 7 nodos, no dirigido

# Agregar aristas según el grafo
graph.add_edge(0, 1)  # Dunwich - Blaxhall
graph.add_edge(0, 2)  # Dunwich - Harwich
graph.add_edge(1, 2)  # Blaxhall - Harwich
graph.add_edge(1, 3)  # Blaxhall - Feering
graph.add_edge(2, 4)  # Harwich - Tiptree
graph.add_edge(2, 5)  # Harwich - Clacton
graph.add_edge(3, 4)  # Feering - Tiptree
graph.add_edge(3, 6)  # Feering - Maldon
graph.add_edge(4, 5)  # Tiptree - Clacton
graph.add_edge(4, 6)  # Tiptree - Maldon
graph.add_edge(5, 6)  # Clacton - Maldon

graph.show_graph_matriz()

print("BFS (rec):", graph.bfs(0))  # Desde Dunwich
print("BFS (no recursiva):", graph.bfs_non_recursive(0))  # Desde Dunwich
