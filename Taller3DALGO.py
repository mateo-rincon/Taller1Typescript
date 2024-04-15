class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def kruskal(n, edges):
    mst_weight = 0
    ds = DisjointSet(n)
    # Ordenar aristas por peso
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for u, v, weight in sorted_edges:
        # Si u y v no están conectados, añadir esta arista al MST
        if ds.find(u - 1) != ds.find(v - 1):  # Ajustar índices a base 0
            ds.union(u - 1, v - 1)
            mst_weight += weight
    return mst_weight

# Datos de entrada
n, m = 5, 7  # Número de vértices y aristas
edges = [
    (1, 2, 3),
    (1, 3, 5),
    (2, 3, 2),
    (2, 4, 7),
    (3, 4, 1),
    (3, 5, 4),
    (4, 5, 6)
]

# Calcular el peso total del MST
print(kruskal(n, edges))



import heapq

def dijkstra(n, edges, start):
    # Crear un grafo a partir de las aristas
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u-1].append((v-1, w))  # Ajustar a base 0
        graph[v-1].append((u-1, w))  # Asumir grafo no dirigido

    # Inicializar distancias: infinito para todos excepto el nodo de inicio
    distances = [float('inf')] * n
    distances[start-1] = 0  # Ajustar a base 0

    # Usar una cola de prioridad para almacenar (distancia, nodo)
    queue = [(0, start-1)]  # Ajustar a base 0
    while queue:
        dist, current = heapq.heappop(queue)
        if dist > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # La distancia total será la suma de todas las distancias mínimas
    total_distance = sum(distances)
    return total_distance

# Ejemplo de datos de entrada
n = 5  # Número de computadoras
edges = [
    (1, 2, 1), (1, 3, 4), (2, 3, 2),
    (2, 4, 7), (3, 4, 3), (3, 5, 1),
    (4, 5, 1)
]
start = 1  # Computadora que envía el mensaje broadcast

# Calcular la distancia total más corta
total_distance = dijkstra(n, edges, start)
print(total_distance)