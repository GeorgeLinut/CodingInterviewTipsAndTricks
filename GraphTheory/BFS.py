class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_iter(self, start):
        visited = [False] * len(self.graph)
        q = []
        q.append(start)
        visited[start] = True
        while q:
            current = q.pop(0)
            print(current)
            for i in self.graph[current]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True


b = Graph(4)
b.add_edge(0, 1)
b.add_edge(0, 2)
b.add_edge(1, 2)
b.add_edge(2, 0)
b.add_edge(2, 3)

b.bfs_iter(2)