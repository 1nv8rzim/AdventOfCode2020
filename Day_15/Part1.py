with open("Day_15/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

data = [int(_num) for _num in data[0].split(',')]

while len(data) < 2020:
    newest = data[-1]
    if newest not in data[:-1]:
        data.append(0)
        continue
    else:
        data.append(data[:-1][::-1].index(newest) + 1)

print(data[-1])
