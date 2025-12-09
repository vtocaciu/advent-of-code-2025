def read_input():
    coordinates = []

    with open("input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            x, y = map(int, line.strip().split(','))
            coordinates.append((x, y))
    return coordinates



def print_grid(grid):
    for row in grid:
        print(''.join(row))


def is_valid_rectangle(c1, c2, grid, x_index, y_index):
    x1, y1 = c1
    x2, y2 = c2
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    for y in range(y_index[min_y], y_index[max_y]+1):
        for x in range(x_index[min_x], x_index[max_x]+1):
            if grid[y][x] == '.':
                return False
    return True


def sparse_get_grid(coordinates):
    x_coords = []
    y_coords = []
    for x, y in coordinates:
        if x not in x_coords:
            x_coords.append(x)
        if y not in y_coords:
            y_coords.append(y)
    x_coords = sorted(x_coords)
    y_coords = sorted(y_coords)

    x_index = {}
    y_index = {}

    for idx, x in enumerate(x_coords):
        x_index[x] = 2 * idx + 2 # leave space for borders and add some space between points
    for idx, y in enumerate(y_coords):
        y_index[y] = 2 * idx + 2

    grid_size_x = 2 * len(x_coords) + 5 # extra space for borders
    grid_size_y = 2 * len(y_coords) + 5
    grid = []
    for i in range(grid_size_y):
        row = []
        for j in range(grid_size_x):
            row.append('?') # unknown tile
        grid.append(row)

    for x, y in coordinates:
        grid[y_index[y]][x_index[x]] = '#' # red tile

    def fill_line(first, second):
        min_x = min(first[0], second[0])
        max_x = max(first[0], second[0])
        min_y = min(first[1], second[1])
        max_y = max(first[1], second[1])
        for y in range(y_index[min_y], y_index[max_y]+1):
            for x in range(x_index[min_x], x_index[max_x]+1):
                grid[y][x] = '#' # green tile

    # trace the polygon boundary
    for i in range(len(coordinates) - 1):
        fill_line(coordinates[i], coordinates[i+1])
    fill_line(coordinates[-1], coordinates[0])

    outside_point = [(0, 0)]
    while outside_point:
        x, y = outside_point.pop()
        grid[y][x] = '.' # mark as outside
        # check neighbors
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < grid_size_x and 0 <= ny < grid_size_y:
                if grid[ny][nx] == '?':
                    outside_point.append((nx, ny))

    def flood_fill():
        print(x_index[coordinates[0][0]])
        print(y_index[coordinates[0][1]])
        start_point = [(x_index[coordinates[0][0]], y_index[coordinates[0][1]])]
        while start_point:
            x, y = start_point.pop()
            if grid[y][x] == '?':
                grid[y][x] = '#' # mark as inside
            # check neighbors
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
            for nx, ny in neighbors:
                if 0 <= nx < grid_size_x and 0 <= ny < grid_size_y:
                    if grid[ny][nx] == '?':
                        start_point.append((nx, ny))

    flood_fill()

    print_grid(grid)
    return grid, x_index, y_index



def solve(coordinates):
    grid, x_index, y_index = sparse_get_grid(coordinates)
    area = 0
    for i, coordinate in enumerate(coordinates):
        x, y = coordinate
        for j in range(i+1, len(coordinates)):
            other = coordinates[j]
            other_area = (abs(x - other[0])+1) * (abs(y - other[1]) + 1)
            if other_area > area and is_valid_rectangle(coordinate, other, grid, x_index, y_index):
                area = other_area
    return area

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
