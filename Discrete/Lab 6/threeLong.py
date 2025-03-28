def find_top_three_cycles(graph):
    def dfs(start_v, current_v, parent, visited, path):
        visited[current_v] = True
        path.append(current_v)
        for neighbor in graph[current_v]:
            if neighbor == parent:
                continue
            if neighbor == start_v and len(path) >= 3:
                cycle = path + [neighbor]
                if min(cycle[:-1]) == start_v:
                    cycles.add(normalize_cycle(cycle))
            elif visited[neighbor]:
                pos = path.index(neighbor)
                cycle = path[pos:] + [neighbor]
                if min(cycle[:-1]) == start_v:
                    cycles.add(normalize_cycle(cycle))
            else:
                if neighbor >= start_v:
                    dfs(start_v, neighbor, current_v, visited, path)
        path.pop()
        visited[current_v] = False

    def normalize_cycle(cycle):
        vertices = cycle[:-1]
        if not vertices:
            return tuple()
        min_v = min(vertices)
        min_indices = [i for i, v in enumerate(vertices) if v == min_v]
        candidates = []
        for i in min_indices:
            rotated = vertices[i:] + vertices[:i]
            reversed_rotated = rotated[::-1]
            reversed_min_index = len(rotated) - 1 - i
            reversed_candidate = rotated[::-1]
            reversed_candidate = reversed_candidate[-reversed_min_index:] + reversed_candidate[:-reversed_min_index]
            if rotated[1] <= reversed_rotated[1]:
                candidates.append(rotated)
            else:
                candidates.append(reversed_rotated)
        canonical = min(candidates) if candidates else []
        return tuple(canonical + [canonical[0]])

    cycles = set()
    vertices = sorted(graph.keys())
    for v in vertices:
        visited = {node: False for node in graph}
        dfs(v, v, -1, visited, [])
    sorted_cycles = sorted(cycles, key=lambda x: len(x)-1, reverse=True)
    return [list(cycle) for cycle in sorted_cycles[:3]]


graph = {
    0: [1, 3, 5, 6],
    1: [0, 2, 3],
    2: [1, 3, 4, 7],
    3: [0, 1, 2, 4, 6],
    4: [2, 3, 5],
    5: [0, 4, 6],
    6: [0, 3, 5, 7],
    7: [2, 6]
}
print(find_top_three_cycles(graph))