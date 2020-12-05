with open('../Day_5/input.txt', 'r') as file:
    data = file.readlines()

for index, line in enumerate(data):
    data[index] = int(line.strip().replace('F', '0').replace(
        'B', '1').replace('R', '1').replace('L', '0'), 2)

print(*set(range(85, 883)).difference(set(data)))
