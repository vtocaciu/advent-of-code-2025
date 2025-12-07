from functools import lru_cache


def read_input():
    data = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            data.append([c for c in line])
    print(data)
    return data



def solve(data):
    start_pos = None
    for i, line in enumerate(data):
        for j, chr in enumerate(line):
            if chr == 'S':
                start_pos = (i, j)

    @lru_cache
    def beam(pos):
        n = len(data)
        m = len(data[0])
        i, j = pos
        print(i, j)
        if i == n - 1:
            return 1
        if i >= n or j >= m or j < 0 or i+1 > n:
            return 0
        if data[i+1][j] == '^':
            return beam((i+1, j-1)) + beam((i+1, j+1))
        return beam((i+1, j))

    return beam(start_pos)

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
