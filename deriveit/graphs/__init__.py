class GraphNode:
    @staticmethod
    def of(graph):
        nodes = [GraphNode(graph_node[0], []) for graph_node in graph]
        for adj, node in zip(graph, nodes):
            for neighbor in adj[1:]:
                node.neighbors.append(nodes[neighbor])
        return nodes[0]

    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def __repr__(self):
        # pritnt(GraphNode.of([[0, 1, 2], [1], [2]]))
        # GraphNode.of([[0, 1, 2], [1], [2]])
        return f"GraphNode.of({self.adjacency_list()})"

    def adjacency_list(self):
        visited = set()
        nodes = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            nodes.append(node)
            for neighbor in node.neighbors:
                dfs(neighbor)

        dfs(self)
        sorted_nodes = sorted(nodes, key=lambda node: node.val)

        return [
            [node.val] + [sorted_nodes.index(neighbor) for neighbor in node.neighbors]
            for node in sorted_nodes
        ]
