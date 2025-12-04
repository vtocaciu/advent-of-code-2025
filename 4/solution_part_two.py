def read_input():
    with open("input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def remove(data):
    coordinates = []
    for i, line in enumerate(data):
        for j, object in enumerate(line):
            if object == '.':
                continue
            neighbors = 0
            for plusI, plusJ in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = i + plusI, j + plusJ
                if 0 <= ni < len(data) and 0 <= nj < len(line):
                    if data[ni][nj] == '@':
                        neighbors += 1
            if neighbors < 4:
                coordinates.append((i, j))
    if len(coordinates) == 0:
        return 0, False
    for i, j in coordinates:
        data[i] = data[i][:j] + '.' + data[i][j+1:]
    return len(coordinates), True

def solve(data):
    total_removed = 0
    while True:
        removed, can_continue = remove(data)
        if not can_continue:
            break
        total_removed += removed
    return total_removed


if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
