with open('Day_8/input.txt', 'r') as file:
    data = file.readlines()

_set = set()
accumulator = 0
i = 0

while i < len(data):
    line = data[i]
    if i in _set:
        print('Failed')
        break
    else:
        _set.add(i)

    line = line.split()

    if line[0] == 'acc':
        accumulator += int(line[1])
    elif line[0] == 'jmp':
        i = i + int(line[1])
        continue

    i += 1

print(accumulator)
