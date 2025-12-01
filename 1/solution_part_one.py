

def read_input():
    operations = []
    with open("input.txt", "r") as file:
        for line in file:
            direction = line[0]
            value = int(line[1:])
            operations.append((direction, value))
    return operations

def start(operations):
    current_value = 50
    max_value = 100
    password = 0
    for direction, value in operations:
        if direction == 'R':
            current_value = (current_value + value) % max_value
        elif direction == 'L':
            current_value = current_value - value
        while not (0 <= current_value < max_value):
            print(current_value)
            if current_value < 0:
                current_value = max_value + current_value
            if current_value >= max_value:
                current_value = current_value % max_value
        if current_value == 0:
            password = password + 1
        print(direction, value, current_value)
    return password

if __name__ == '__main__':
    operations = read_input()
    print(start(operations))

