def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()

def solve(lines):
    password = 0
    for line in lines:
        max_number = None
        for idx, digit in enumerate(line.strip()):
            for other_idx, other_digit in enumerate(line.strip()):
                if other_idx <= idx:
                    continue
                if not max_number or int(digit) * 10 + int(other_digit) > max_number:
                    max_number = int(digit) * 10 + int(other_digit)
        password = password + max_number

    return password



if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
