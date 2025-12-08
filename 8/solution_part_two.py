from heapq import heapify, heappush, heappop
from math import sqrt

def read_input():
    circuits = []
    with open("input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip().split(",")
            circuits.append((int(line[0]), int(line[1]), int(line[2])))

    return circuits

def distance(first, second):
    return sqrt((first[0]-second[0])**2 + (first[1]-second[1])**2 + (first[2]-second[2])**2)

def solve(circuits):
    distances = {}
    min_heap = []
    heapify(min_heap)
    for i, circuit in enumerate(circuits):
        for j in range(i + 1, len(circuits)):
            other_circuit = circuits[j]
            dist = distance(circuit, other_circuit)
            if dist in distances.keys():
                # all distances are unique
                print("SHOCKED")
                raise ValueError
            heappush(min_heap, dist)
            distances[dist] = (circuit, other_circuit)
    connections = []
    connected = {}
    last_connection = None
    while min_heap:
        dist = heappop(min_heap)
        circuit_a, circuit_b = distances[dist]

        if circuit_a in connected and circuit_b in connected:
            if connected[circuit_a] == connected[circuit_b]:
                continue
            removed_circuit = connected[circuit_b]
            for conn in connections[removed_circuit]:
                connected[conn] = connected[circuit_a]
                connections[connected[circuit_a]].append(conn)
            last_connection = circuit_a[0]*circuit_b[0]
            connections[removed_circuit] = []
            continue
        last_connection = circuit_a[0]*circuit_b[0]
        if circuit_a in connected:
            connections[connected[circuit_a]].append(circuit_b)
            connected[circuit_b] = connected[circuit_a]
            continue
        if circuit_b in connected:
            connections[connected[circuit_b]].append(circuit_a)
            connected[circuit_a] = connected[circuit_b]
            continue
        connections.append([circuit_a, circuit_b])
        connected[circuit_a] = len(connections) - 1
        connected[circuit_b] = len(connections) - 1
    print("Circuit connections:")
    for connection in connections:
        print(connection)
    return last_connection

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
