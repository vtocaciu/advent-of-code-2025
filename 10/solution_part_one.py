from functools import lru_cache


def read_input():
    buttons = []
    presses = []
    joltages = []
    with open("input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip().split(" ")
            buttons.append(line[0])
            presses.append(line[1:-1])
            joltages.append(line[-1])

    final_buttons = []
    final_presses = []
    final_joltages = []
    for button in buttons:
        button = button[1:-1]
        new_button = []
        for char in button:
            if char == ".":
                new_button.append(0)
            else:
                new_button.append(1)
        final_buttons.append(new_button)

    for press in presses:
        new_press = []
        for pr in press:
            pr = pr[1:-1]
            new_pr = []
            for char in pr.split(","):
                new_pr.append(int(char))
            new_press.append(new_pr)
        final_presses.append(new_press)

    print(final_buttons)
    print(final_presses)
    print(joltages)
    return final_buttons, final_presses

def solve(data):
    buttons, presses = data
    total = 0
    for i in range(len(buttons)):
        button = tuple(buttons[i])
        press = presses[i]
        @lru_cache
        def press_button(index, current_output, presses):
            if button == current_output:
                return presses
            if index >= len(press):
                return float('inf')
            pressing = []
            for idx in range(len(current_output)):
                if idx in press[index]:
                    pressing.append(1 if current_output[idx] == 0 else 0)
                else:
                    pressing.append(current_output[idx])

            return min(press_button(index+1, current_output, presses), press_button(index+1, tuple(pressing), presses+1))
        total = total + press_button(0, tuple([0]*len(button)), 0)
    return total

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
