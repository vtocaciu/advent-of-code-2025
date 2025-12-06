def read_input():
    operations = []
    with open("input.txt", "r") as file:
        data = file.readlines()
        line = data[0].strip()
        print(line, line.split(" "))
        for number in line.split(" "):
            if number:
                operations.append([])
        for line in data:
            line = line.strip()
            current_index = 0
            for index, number in enumerate(line.split(" ")):
                if number:
                    operations[current_index].append(number)
                    current_index = current_index + 1
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
        print(f"{operation} = {result}")
    return final_result

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
