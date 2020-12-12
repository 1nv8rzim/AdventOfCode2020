with open("Day_12/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

for i in range(len(data)):
    data[i] = (data[i][0], int(data[i][1:]))

distance = [0, 0]
orientation = 0
compass = {0: 'E', 90: 'S', 180: 'W', 270: 'N'}

for direction, value in data:
    if direction == 'N':
        distance[0] += value
    elif direction == 'S':
        distance[0] -= value
    elif direction == 'E':
        distance[1] += value
    elif direction == 'W':
        distance[1] -= value
    elif direction == 'L':
        orientation = (orientation - value) % 360
    elif direction == 'R':
        orientation = (orientation + value) % 360
    elif direction == 'F':
        temp_direction = compass[orientation]
        if temp_direction == 'N':
            distance[0] += value
        elif temp_direction == 'S':
            distance[0] -= value
        elif temp_direction == 'E':
            distance[1] += value
        elif temp_direction == 'W':
            distance[1] -= value

print(distance[0], distance[1], abs(distance[1]) + abs(distance[0]))
