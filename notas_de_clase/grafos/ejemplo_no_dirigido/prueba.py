from grafo_matriz import grafo_matriz

mi_grafo = grafo_matriz(5)
mi_grafo.show_graph_matriz()

print("-------------")

mi_grafo.add_edge(0,1)
mi_grafo.add_edge(0,4)
mi_grafo.add_edge(1,4)
mi_grafo.add_edge(1,3)
mi_grafo.add_edge(1,2)
mi_grafo.add_edge(4,3)
mi_grafo.add_edge(3,2)
mi_grafo.show_graph_matriz()

print("-------------")
print(mi_grafo.list_adyacency(0))
print("-------------")
print(mi_grafo.list_adyacency(1))