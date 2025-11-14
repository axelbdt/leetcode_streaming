# Directed graph

# adjacency list
graph_1_list = [[], [0, 2], [0, 3], [], [2]]

# adjacency matrix
graph_1_matrix = [
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]

# Nb nodes + Arc list
graph_1_arcs = (5, [(1, 0), (1, 2), (2, 0), (2, 3), (4, 2)])


# graph 2
graph_2_list = [[2, 3], [0], [4], [], []]


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


def search(graph, node, bag):
    visited = []
    bag.push(node)

    while not bag.isEmpty():
        v = bag.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                bag.push(w)

    return visited


def dfs_it(graph, node):
    return search(graph, node, Stack())


def bfs(graph, node):
    return search(graph, node, Queue())


print(dfs_it(graph_1_list, 0))

print(dfs_it(graph_2_list, 0))
print(bfs(graph_2_list, 0))


# recursive version dfs
def dfs(graph, node):
    visited = []
    if node not in visited:
        visited.append(node)
        for w in graph[node]:
            dfs(graph, w)
    return visited


def dfs_all(graph):
    visited = []
    for i in range(len(graph)):
        if dfs(graph, i) not in visited:
            visited.append(dfs(graph, i))
    return visited


print(dfs_all(graph_1_list))
print(dfs_all(graph_2_list))
