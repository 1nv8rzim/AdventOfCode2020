with open("Day_13/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

bus, delay = [], []

for index, line in enumerate(data[1].split(',')):
    if line == 'x':
        continue
    _bus = int(line)
    bus.append(_bus)
    delay.append((_bus - index) % _bus)


def func(delay, _bus):
    if delay == _bus + 1:
        return 1, -1
    a, b = delay//_bus, delay % _bus
    c, d = func(_bus, b)
    return d, c - d * a


product = 1

for _bus in bus:
    product *= _bus

answer = 0

for index, _bus in enumerate(bus):
    a, b = func(product // _bus, _bus)
    answer += delay[index] % _bus * a * product // _bus

print(answer % product)
