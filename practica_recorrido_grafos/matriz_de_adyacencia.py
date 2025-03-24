# Definir los nodos
nodes = ['Berkeley', 'Sacramento', 'San Francisco', 'San Jose', 'Pleasanton', 'Concord', 'Los Angeles', 'Tracy', 'Merced', 'Modesto', 'Stockton']

# Definir las aristas con sus valores
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

# Inicializar matrices
adjacency_matrix_binary = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
adjacency_matrix_with_weights = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]

# Poblar las matrices
for src, dst, weight in edges:
    src_index = node_indices[src]
    dst_index = node_indices[dst]
    
    # Matriz binaria
    adjacency_matrix_binary[src_index][dst_index] = 1
    adjacency_matrix_binary[dst_index][src_index] = 1
    
    # Matriz con pesos
    adjacency_matrix_with_weights[src_index][dst_index] = weight
    adjacency_matrix_with_weights[dst_index][src_index] = weight

# Imprimir la matriz binaria
print("Matriz binaria:")
print("- Números de fila y columna representan los índices de los nodos.")
print("- Valores:\n   - 0: No hay conexión directa.\n   - 1: Hay conexión directa.\n")
print("      1  2  3  4  5  6  7  8  9  10 11")
print("    _________________________________")
for i, row in enumerate(adjacency_matrix_binary, start=1):
    print(f"{i:2} |", end="")
    for val in row:
        print(f"{val:3}", end="")
    print()

# Imprimir la matriz con pesos
print("\nMatriz con valor de aristas:")
print(" - Números de fila y columna representan los índices de los nodos.")
print(" - Valores:\n   - X: no hay conexión directa.\n   - Número: valor de la arista.\n")
print("       1   2   3   4   5   6   7   8   9   10  11")
print("    ____________________________________________")
for i, row in enumerate(adjacency_matrix_with_weights, start=1):
    print(f"{i:2} |", end="")
    for val in row:
        if val == 0:
            print(f"   X", end="") # Imprimir 'X' si no hay conexión
        else:
            print(f"{val:4}", end="")
    print()

print("\nLeyenda de nodos:")
for i, node in enumerate(nodes, start=1):
    print(f"{i} = {node}")
