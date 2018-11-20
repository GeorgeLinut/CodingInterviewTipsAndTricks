class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursiv(self, start, visited):
        visited[start] = True
        print(start)

        for i in self.graph[start]:
            if not visited[i]:
                self.dfs_recursiv(i, visited)

    def dfs_main(self, start):
        visited = [False] * len(self.graph)
        self.dfs_recursiv(start, visited)


b = Graph(4)
b.add_edge(0, 1)
b.add_edge(0, 2)
b.add_edge(1, 2)
b.add_edge(2, 0)
b.add_edge(2, 3)

b.bfs_iter(2)
print()
b.dfs_iter(2)