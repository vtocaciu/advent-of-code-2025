from collections import defaultdict


def read_input():
    numbers=[]
    with open("input.txt", "r") as file:
        ranges=file.read().split(",")
        for range in ranges:
            first,second = range.split("-")[0], range.split("-")[1]
            numbers.append((int(first),int(second)))
    return numbers

from collections import defaultdict

def solve(numbers):
    password = 0
    for first, second in numbers:
        for number in range(first, second+1):
            counter = defaultdict(int)
            strnumber = str(number)
            if len(strnumber) == 2:
                if strnumber[0] == strnumber[1]:
                    password += number
                    #print(number)
                    continue
            if len(set([strdigit for strdigit in strnumber])) == 1 and number > 9:
                password += number
                #print(number)
                continue
            for sequence_length in range(2, len(strnumber)//2+1):
                if len(strnumber) % sequence_length:
                    continue
                sequence = strnumber[:sequence_length]
                repetitions = len(strnumber) // sequence_length
                if sequence * repetitions == strnumber:
                    password += number
                    #print(number, sequence)
                    break
    return password

if __name__ == '__main__':
    numbers = read_input()
    result = solve(numbers)
    print(result)
