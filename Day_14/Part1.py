with open("Day_14/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

mask = 0
mem = [0 for x in range(100000)]


def apply_mask(num, _mask):
    num = bin(int(num))[2:]
    while len(num) < 36:
        num = '0' + num
    num = list(num)
    zeros, ones = [i for i, x in enumerate(_mask) if x == "0"], [
        i for i, x in enumerate(_mask) if x == "1"]
    for i in zeros:
        num[i] = '0'
    for i in ones:
        num[i] = '1'
    return int(''.join(num), 2)


for line in data:
    line = line.split(' = ')
    if line[0][:3] == 'mem':
        mem[int(line[0][4:-1])] = apply_mask(line[1], mask)
    else:
        mask = line[1]

_sum = 0

for line in mem:
    _sum += line

print(_sum)
