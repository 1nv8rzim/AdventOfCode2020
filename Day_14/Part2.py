with open("Day_14/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

mask = 0
mem = {}

TEST = True


def floats(num):
    if 'X' not in num:
        return [num]
    else:
        alt = num[:]
        alt[alt.index('X')] = '0'
        num[num.index('X')] = '1'
        return [] + floats(alt) + floats(num)


def apply_mask(num, _mask):
    num = bin(int(num))[2:]
    while len(num) < 36:
        num = '0' + num
    num = list(num)
    ones, floating = [i for i, x in enumerate(_mask) if x == "1"], [
        i for i, x in enumerate(_mask) if x == "X"]
    for i in ones:
        num[i] = '1' if num[i] == '0' else '0'
    for i in floating:
        num[i] = 'X'
    return list(set([int(''.join(_num), 2) for _num in floats(num)]))


for line in data:
    line = line.split(' = ')
    if line[0][:3] == 'mem':
        for i in apply_mask(int(line[0][4:-1]), mask):
            mem[i] = int(line[1])
    else:
        mask = line[1]

_sum = 0

for line in mem:
    _sum += mem[line]

print(_sum)
