def read_input():
    coordinates = []
    with open("input.txt", "r") as file:
        data = file.readlines()
        for line in data:
            x, y = map(int, line.strip().split(','))
            coordinates.append((x, y))
    print(len(coordinates))

    return coordinates

def solve(coordinates):
    coordinates = sorted(coordinates, key=lambda a:(a[0], a[1]))
    area = 0
    for i, coordinate in enumerate(coordinates):
        x, y = coordinate
        for j in range(i+1, len(coordinates)):
            other = coordinates[j]
            other_area = (abs(x - other[0])+1) * (abs(y - other[1]) + 1)
            #print(coordinate, other, other_area)
            area = max(area, other_area)
    return area

if __name__ == '__main__':
    data = read_input()
    result = solve(data)
    print(result)
