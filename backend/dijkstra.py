import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_solution(self, dist):
        print("Distancia del nodo fuente a cada uno de los otros nodos:")
        for node in range(self.V):
            print(f"Nodo {node} \t\t Distancia={dist[node]}")

    def min_distance(self, dist, visitados):
        min_val = sys.maxsize
        for v in range(self.V):
            if dist[v] < min_val and visitados[v] == False:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        visitados = [False] * self.V

        for cout in range(self.V):
            u = self.min_distance(dist, visitados)
            visitados[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and visitados[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)