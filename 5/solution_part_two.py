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
    concat_ranges = ranges
    can_concat = True
    while can_concat:
        can_concat = False
        new_concat_ranges = []
        i = 0
        while i < len(concat_ranges):
            first, second = concat_ranges[i]
            j = i + 1
            while j < len(concat_ranges):
                next_first, next_second = concat_ranges[j]
                if next_first <= second + 1:
                    second = max(second, next_second)
                    can_concat = True
                else:
                    break
                j += 1
            new_concat_ranges.append((first, second))
            i = j
        concat_ranges = new_concat_ranges
    fresh = 0
    for first, second in concat_ranges:
        fresh = fresh + second - first + 1
    return fresh


if __name__ == '__main__':
    ranges, ids = read_input()
    result = solve(ranges, ids)
    print(result)
