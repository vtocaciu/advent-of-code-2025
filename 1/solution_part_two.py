def read_input():
    operations = []
    with open("input.txt", "r") as file:
        for line in file:
            direction = line[0]
            value = int(line[1:])
            operations.append((direction, value))
    return operations

def click(current_value, max_value, clicks, direction):
    zero_clicked = 0
    for _ in range(clicks):
        current_value = current_value + direction
        if current_value == max_value:
            current_value = 0
        if current_value == -1:
            current_value = max_value - 1
        if current_value == 0:
            zero_clicked = zero_clicked + 1
    return current_value, zero_clicked

def start(operations):
    current_value = 50
    max_value = 100
    password = 0
    zero_clicked = 0
    for direction, value in operations:
        if direction == 'R':
            current_value, zero_clicked = click(current_value, max_value, value, 1)
        elif direction == 'L':
            current_value, zero_clicked = click(current_value, max_value, value, -1)
        password = password + zero_clicked

        print(direction, value, current_value, password)
    return password

if __name__ == '__main__':
    operations = read_input()
    print(start(operations))

