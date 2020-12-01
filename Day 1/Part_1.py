with open('Day 1/Part 1/input.txt', 'r') as input:
    data = [int(line.strip()) for line in input]

for index, i in enumerate(data):
    for j in data[i+1:]:
        if i + j == 2020:
            print(i, j, i * j)
