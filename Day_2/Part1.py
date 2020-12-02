with open('../Day_2/input.txt', 'r') as file:
    data = [line.strip().split() for line in file]

for i, element in enumerate(data):
    data[i][1] = element[1][0]
    data[i][0] = element[0].split('-')

print(sum(int(line[0][0]) <= line[2].count(
    line[1]) <= int(line[0][1]) for line in data))
