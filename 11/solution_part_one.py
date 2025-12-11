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
    start_node = 'you'
    end_node = 'out'

    def dfs(node, visited):
        if node == end_node:
            return 1
        if node in visited:
            return 0

        visited.add(node)
        count = 0
        for next_node in graph.get(node, []):
            count += dfs(next_node, visited)
        visited.remove(node)
        return count

    return dfs(start_node, set())

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
