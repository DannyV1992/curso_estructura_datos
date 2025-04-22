class grafo_matriz:
    def __init__(self, node_qty, is_directed):
        self.__matriz = []
        for _ in range(node_qty):
            self.__matriz.append([0] * node_qty)
        self.__is_directed = is_directed

    def show_graph_matriz(self):
        for row in self.__matriz:
            print(row)

    def add_edge(self, src, dst):
        self.__matriz[src][dst] = 1
        if not self.__is_directed:
            self.__matriz[dst][src] = 1

    def list_adyacency(self, node):
        adyacency_list = []
        for col in range(len(self.__matriz)):
            if self.__matriz[node][col] == 1: 
                adyacency_list.append(col)
        return adyacency_list

    # DFS Recursiva
    def dfs(self, start_node):
        visited = [False] * len(self.__matriz)
        result = []

        def dfs_recursive(node):
            visited[node] = True
            result.append(node)
            print(f"Visiting: {node}")

            decision_point = False
            for neighbor in self.list_adyacency(node):
                if not visited[neighbor]:
                    if decision_point:
                        print(f"Decision Point: Returning to {node} to explore new path")
                    dfs_recursive(neighbor)
                    decision_point = True

        dfs_recursive(start_node)
        return result

    # DFS - NR
    def dfs_non_recursive(self, start_node):
        visited = [False] * len(self.__matriz)
        stack = [start_node]
        result = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                result.append(node)
                print(f"Visita: {node}")

                decision_point = False
                for neighbor in reversed(self.list_adyacency(node)):
                    if not visited[neighbor]:
                        if decision_point:
                            print(f"Decision: Return to {node} to explore new path")
                        stack.append(neighbor)
                        decision_point = True

        return result

    # BFS Rec
    def bfs(self, start_node):
        visited = [False] * len(self.__matriz)
        queue = [(start_node, 0)]  # Tuple to track (node, level)
        visited[start_node] = True
        result = []
        level_structure = {}  # Dictionary to group nodes by level

        while queue:
            current_node, level = queue.pop(0)
            if level not in level_structure:
                level_structure[level] = []
            level_structure[level].append(current_node)

            for neighbor in self.list_adyacency(current_node):
                if not visited[neighbor]:
                    queue.append((neighbor, level + 1))
                    visited[neighbor] = True

        # Print nodes by levels
        for lvl in sorted(level_structure.keys()):
            print(f"Level {lvl}: {level_structure[lvl]}")

        return result

    # Breadth-First Search (BFS) NR
    def bfs_non_recursive(self, start_node):
        visited = [False] * len(self.__matriz)
        queue = [(start_node, 0)]  # (node, level)
        visited[start_node] = True
        level_structure = {}  # Dictionary to group nodes by level

        while queue:
            node, level = queue.pop(0)
            if level not in level_structure:
                level_structure[level] = []
            level_structure[level].append(node)

            for neighbor in self.list_adyacency(node):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, level + 1))

        # Print nodes by levels
        for lvl in sorted(level_structure.keys()):
            print(f"Level {lvl}: {level_structure[lvl]}")