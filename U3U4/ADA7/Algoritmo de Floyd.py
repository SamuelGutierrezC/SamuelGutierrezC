import sys

INF = sys.maxsize


def Floyd_Warshall(graph):
    n = len(graph)
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print('Distancia más corta entre cada par de nodos:')
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=' ')
            else:
                print("%7s" % (dist[i][j]), end=' ')
        print()
graph = [
    [0, 700, 200, INF, INF, INF],
    [700, 0, 300, 200, INF, 400],
    [200, 300, 0, 700, 600, INF],
    [INF, 200, 700, 0, 300, 100],
    [INF, INF, 600, 300, 0, 500],
    [INF, 400, INF, 100, 500, 0]
]

Floyd_Warshall(graph)
