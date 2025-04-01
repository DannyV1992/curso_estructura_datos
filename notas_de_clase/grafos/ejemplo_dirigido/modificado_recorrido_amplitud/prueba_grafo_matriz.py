from grafo_matriz import grafo_matriz

graph = grafo_matriz(6, False) # Si es dirigido es False, si no es dirigido es True
graph.add_edge(0, 4)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 4)
graph.add_edge(4, 3)
graph.add_edge(3, 5)

graph.show_graph_matriz()
print("DFS (recursiva):", graph.dfs(0))
print("DFS (no recursiva):", graph.dfs_non_recursive(0))
print("BFS (rec):", graph.bfs(1))
print("BFS (no recursiva):", graph.bfs_non_recursive(1))