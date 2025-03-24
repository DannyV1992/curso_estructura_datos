# Definir los nodos
nodes = ['Berkeley', 'Sacramento', 'San Francisco', 'San Jose', 'Pleasanton', 'Concord', 'Los Angeles', 'Tracy', 'Merced', 'Modesto', 'Stockton']

# Definir las aristas con sus pesos
edges = [
    ('Berkeley', 'Sacramento', 80),
    ('Berkeley', 'San Francisco', 80),
    ('Berkeley', 'San Jose', 880),
    ('Berkeley', 'Pleasanton', 580),
    ('Berkeley', 'Concord', 24),
    ('San Jose', 'San Francisco', 101),
    ('San Jose', 'Los Angeles', 101),
    ('San Jose', 'Pleasanton', 680),
    ('Los Angeles', 'Tracy', 5),
    ('Los Angeles', 'Merced', 99),
    ('Merced', 'Modesto', 99),
    ('Modesto', 'Stockton', 99),
    ('Modesto', 'Tracy', 132),
    ('Stockton', 'Sacramento', 99),
    ('Stockton', 'Concord', 4),
    ('Stockton', 'Tracy', 5),
    ('Pleasanton', 'Concord', 680),
    ('Pleasanton', 'Tracy', 580)
]

# Crear un diccionario para mapear nodos a índices
node_indices = {node: index for index, node in enumerate(nodes)}

# Inicializar la matriz de adyacencia con ceros
adjacency_matrix = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]

# Poblar la matriz de adyacencia
for src, dst, _ in edges:
    src_index = node_indices[src]
    dst_index = node_indices[dst]
    adjacency_matrix[src_index][dst_index] = 1
    adjacency_matrix[dst_index][src_index] = 1 

# Imprimir la matriz
print("      1  2  3  4  5  6  7  8  9  10 11")
print("    _________________________________")  # Línea horizontal debajo del encabezado

for i, row in enumerate(adjacency_matrix, start=1):
    print(f"{i:2} |", end="")  # Imprimir número de fila con separador vertical
    for val in row:
        print(f"{val:3}", end="")  # Imprimir valores de la fila
    print()  # Nueva línea al final de cada fila

# Mostrar la notas
print("\nNota:")
print("  - Números de fila y columna representan los índices de los nodos.")
print("  - 0: No hay conexión directa entre los nodos.")
print("  - 1: Hay conexión directa entre los nodos.")

# Mostrar la leyenda de nodos
print("\nLeyenda de nodos:")
for i, node in enumerate(nodes, start=1):
    print(f"{i} = {node}")
