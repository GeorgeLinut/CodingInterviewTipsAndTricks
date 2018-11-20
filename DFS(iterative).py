class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_iter(self, start):
        visited = [False] * len(self.graph)
        st = []
        st.append(start)
        while st:
            current = st.pop()
            if not visited[current]:
                print(current)
                visited[current] = True
            for i in self.graph[current]:
                if not visited[i]:
                    st.append(i)

b = Graph(4)
b.add_edge(0, 1)
b.add_edge(0, 2)
b.add_edge(1, 2)
b.add_edge(2, 0)
b.add_edge(2, 3)

b.dfs_iter(2)