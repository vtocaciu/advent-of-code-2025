def read_input():
    numbers = []
    with (open("input.txt", "r") as file):
        data = file.readlines()
        m = len(data)
        n = max(len(line) for line in data)
        current_index = 0
        numbers.append([])
        for j in range(n):
            number = 0
            is_space = True
            for i in range(m):
                if i >= len(data) or j >= len(data[i]):
                    break
                if data[i][j].strip()!='' and data[i][j].strip().isdigit():
                    number = number * 10 + int(data[i][j].strip())
                    is_space = False

            if is_space:
                numbers.append([])
                current_index = current_index + 1
            else:
                numbers[current_index].append(number)


    operations = []
    numbers = numbers[:-1]
    for line in data[-1]:
        if line == '*' or line == '+':
            operations.append(line)
    print(numbers, operations)
    for index, number_list in enumerate(numbers):
        number_list.append(operations[index])
        operations[index] = number_list
    return operations

def solve(operations):
    final_result = 0
    for operation in operations:
        operator = operation[-1]
        if operator == "+":
            result = 0
        else:
            result = 1
        for number in operation[:-1]:
            if operator == '+':
                result = result + int(number)
            elif operator == '*':
                result = result * int(number)
        final_result = final_result + result
        #print(f"{operation} = {result}")
    return final_result


if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
