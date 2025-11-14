def num_nodes(node):
    visited = set()

    def dfs_count(node):
        if node in visited:
            return 0
        visited.add(node)
        return 1 + sum(dfs_count(neighbor) for neighbor in node.neighbors)

    return dfs_count(node)
