import random
from collections import deque


#Алгоритм Форда-Фалкерсона
def max_flow_min_cut(graph, source, destination):
    # Инициализация остаточной сети
    residual = {}
    nodes = set()
    for edge in graph:
        u, v = edge.split('-')
        nodes.update([u, v])
        if u not in residual:
            residual[u] = {}
        residual[u][v] = graph[edge]
        # Добавляем обратное ребро с нулевой пропускной способностью
        if v not in residual:
            residual[v] = {}
        residual[v][u] = 0

    # Функция для поиска увеличивающего пути через BFS
    def bfs():
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v in residual[u]:
                if v not in visited and residual[u][v] > 0:
                    parent[v] = u
                    visited.add(v)
                    queue.append(v)
                    if v == destination:
                        break
        return parent if destination in visited else None

    # Находим максимальный поток
    max_flow = 0
    while True:
        parent = bfs()
        if not parent:
            break

        #if max_flow == 0:
        #    print(f'parent: {parent}')

        #print(f'residual: {residual}')

        # Находим минимальную пропускную способность в пути(т.е. поток текущего пути)
        path_flow = float('inf')
        v = destination
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # Обновляем остаточную сеть
        v = destination
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        max_flow += path_flow

    # Находим минимальный разрез через достижимые узлы в остаточной сети
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        u = queue.popleft()
        for v in residual[u]:
            if v not in visited and residual[u][v] > 0:
                visited.add(v)
                queue.append(v)

    # Собираем рёбра минимального разреза из исходного графа
    min_cut = []
    for edge in graph:
        u, v = edge.split('-')
        if u in visited and v not in visited:
            min_cut.append((u, v, graph[edge]))

    return max_flow, min_cut


# Граф
graph = {
    's-1': 15,
    's-2': 30,
    's-3': 15,
    '1-4': 11,
    '2-1': 16,
    '2-4': 15,
    '2-7': 15,
    '3-2': 15,
    '3-5': 10,
    '3-8': 20,
    '4-6': 25,
    '4-7': 10,
    '5-2': 10,
    '6-t': 10,
    '7-5': 13,
    '7-6': 10,
    '7-9': 10,
    '7-t': 14,
    '8-7': 12,
    '8-9': 10,
    '9-t': 10,
}

source = 's'
destination = 't'

max_flow, min_cut = max_flow_min_cut(graph, source, destination)

print(f"Максимальный поток: {max_flow}")
print("Минимальный разрез:")
for u, v, cap in min_cut:
    print(f"{u} → {v} (пропускная способность: {cap})")

print()

#Задаем случайные значения
for i in graph:
    graph[i] = random.randint(100, 1000)

max_flow, min_cut = max_flow_min_cut(graph, source, destination)

print(f"Максимальный поток: {max_flow}")
print("Минимальный разрез:")
for u, v, cap in min_cut:
    print(f"{u} → {v} (пропускная способность: {cap})")