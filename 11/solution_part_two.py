from functools import lru_cache


def read_input():
    graph = {}
    with open("input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            parts = line.strip().split(": ")
            node = parts[0]
            edges = parts[1].split(" ")
            graph[node] = edges
    print(graph)
    return graph

def solve(graph):
    start_node = 'svr'
    end_node = 'out'

    @lru_cache(maxsize=None)
    def dfs(node, dac_visited, fft_visited):
        if node == end_node:
            return 1 if dac_visited and fft_visited else 0

        count = 0
        dac_visited = dac_visited or node == 'dac'
        fft_visited = fft_visited or node == 'fft'
        for next_node in graph.get(node, []):
            count += dfs(next_node, dac_visited, fft_visited)
        return count

    return dfs(start_node, False, False)

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
