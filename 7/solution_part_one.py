def read_input():
    data = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)
    print(data)
    return data

def solve(data):
    start_pos = None
    for i, line in enumerate(data):
        for j, chr in enumerate(line):
            if chr == 'S':
                start_pos = (i, j)
    visited = set()
    split = 0
    q = [start_pos]
    n = len(data)
    m = len(data[0])
    while q:
        pos = q.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if i >= n or j >= m or j < 0:
            continue
        next_pos = (i+1, j)
        if next_pos[0] >= n:
            continue
        if data[next_pos[0]][next_pos[1]] == '^':
            q.append((i+1, j-1))
            q.append((i+1, j+1))
            split += 1
        else:
            q.append(next_pos)



    return split

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
