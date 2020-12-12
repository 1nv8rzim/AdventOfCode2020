
from os import wait


with open("Day_12/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

for i in range(len(data)):
    data[i] = (data[i][0], int(data[i][1:]))

distance = [0, 0]
waypoint = [10, 1]

for direction, value in data:
    if direction == 'N':
        waypoint[1] += value
    elif direction == 'S':
        waypoint[1] -= value
    elif direction == 'E':
        waypoint[0] += value
    elif direction == 'W':
        waypoint[0] -= value
    elif direction == 'L':
        value = value % 360
        if value == 0:
            pass
        elif value == 90:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif value == 180:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif value == 270:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    elif direction == 'R':
        value = value % 360
        if value == 0:
            pass
        elif value == 90:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif value == 180:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif value == 270:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif direction == 'F':
        distance[0] += value * waypoint[0]
        distance[1] += value * waypoint[1]

print(distance[0], distance[1], abs(distance[1]) + abs(distance[0]))
