class WarshallAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def warshall(self):
        closure = [row[:] for row in self.graph]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

        return closure


graph = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

warshall_algo = WarshallAlgorithm(graph)
closure = warshall_algo.warshall()
print("Matriz de cierre transitivo:")
for row in closure:
    print(row)
