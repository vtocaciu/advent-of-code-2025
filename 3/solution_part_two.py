def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def max_number_each_line(line):
    max_number = int(line[:12])
    for digit in line[12:].strip():
        max_number_str = str(max_number)
        digit = int(digit)
        for i in range(12):
            candidate_str = max_number_str[:i] + max_number_str[i+1:] + str(digit)
            candidate = int(candidate_str)
            if candidate > max_number:
                max_number = candidate
                break

    return max_number



def solve(lines):
    password = 0
    for idx, line in enumerate(lines):
        max_number = max_number_each_line(line)
        password = password + max_number

    return password



if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
