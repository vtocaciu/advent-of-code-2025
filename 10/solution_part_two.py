from z3 import *

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
    for joltage in joltages:
        joltage = joltage[1:-1]
        jlt = []
        for jolt in joltage.split(","):
            jlt.append(int(jolt))
        final_joltages.append(jlt)

    return final_joltages, final_presses

def solve(data):
    joltages, presses = data
    total = 0
    for i in range(len(joltages)):
        def press_button(presses, targets):
            n_presses = len(presses)

            voltages = [Int(f'p{i}') for i in range(n_presses)]

            opt = Optimize() # thanks microsoft magic for optimization solver fuck knows

            for p in voltages:
                opt.add(p >= 0)

            for counter_idx, target in enumerate(targets):
                contribution = Sum([voltages[idx]
                                    for idx, counters in enumerate(presses)
                                    if counter_idx in counters])
                opt.add(contribution == target)

            opt.minimize(Sum(voltages))

            if opt.check() == sat:
                model = opt.model()
                return sum(model[p].as_long() for p in voltages)
            return float('inf')
        total = total + press_button(presses[i], joltages[i])
    return total

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
