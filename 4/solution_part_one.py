def read_input():
    with open("input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def solve(data):
    free_rolls = 0
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
                free_rolls += 1
    return free_rolls


if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
