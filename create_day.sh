#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

DAY_NUM=$1

mkdir -p "$DAY_NUM"

touch "$DAY_NUM/input.txt"
touch "$DAY_NUM/small_input.txt"

# Create solution_part_one.py with boilerplate
cat > "$DAY_NUM/solution_part_one.py" << 'EOF'
def read_input():
    with open("input.txt", "r") as file:
        data = file.read().strip()
    return data

def solve(data):
    # Your solution here
    pass

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
EOF

# Create solution_part_two.py with boilerplate
cat > "$DAY_NUM/solution_part_two.py" << 'EOF'
def read_input():
    with open("input.txt", "r") as file:
        data = file.read().strip()
    return data

def solve(data):
    # Your solution here
    pass

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
EOF

echo "Created directory: $DAY_NUM"
echo "Created files with boilerplate code!"