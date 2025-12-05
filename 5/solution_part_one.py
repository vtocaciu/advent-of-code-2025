def read_input():
    ranges = []
    ids = []
    is_range = True
    with open("input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip()
            if not line:
                continue
            if "-" not in line:
                is_range = False
            if is_range:
                first, second = line.split("-")[0], line.split("-")[1]
                ranges.append((int(first), int(second)))
            else:
                ids.append(int(line))
    return ranges, ids

def solve(ranges, ids):
    ranges = sorted(ranges, key=lambda x: x[0])
    fresh = 0
    for id in ids:
        for first, second in ranges:
            if first <= id <= second:
                fresh += 1
                break

    return fresh

if __name__ == '__main__':
    ranges, ids = read_input()
    result = solve(ranges, ids)
    print(result)
