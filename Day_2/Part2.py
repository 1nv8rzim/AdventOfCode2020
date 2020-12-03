with open('Day_2/input.txt', 'r') as file:
    data = [line.strip().split() for line in file]

for i, element in enumerate(data):
    data[i][1] = element[1][0]
    data[i][0] = element[0].split('-')

print(sum(((line[2][int(line[0][0]) - 1] == line[1]) ^ (
    line[2][int(line[0][1]) - 1] == line[1]) for line in data)))

valid = 0

for line in data:
    i, j = line[0]
    i, j = int(i) - 1, int(j) - 1

    password = line[2]

    letter = line[1]

    try:
        i = password[i] == letter
    except:
        i = False

    try:
        j = password[j] == letter
    except:
        j = False

    if i ^ j:
        valid -= -1

print(valid)
