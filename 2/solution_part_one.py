def read_input():
    numbers=[]
    with open("input.txt", "r") as file:
        ranges=file.read().split(",")
        for range in ranges:
            first,second = range.split("-")[0], range.split("-")[1]
            numbers.append((int(first),int(second)))
    return numbers

def solve(numbers):
    password = 0
    for first, second in numbers:
        for number in range(first, second+1):
            strnumber = str(number)
            first_half = strnumber[:len(strnumber)//2]
            second_half = strnumber[len(strnumber)//2:]
            if first_half == second_half:
                password += number
    return password

if __name__ == '__main__':
    numbers = read_input()
    result = solve(numbers)
    print(result)
