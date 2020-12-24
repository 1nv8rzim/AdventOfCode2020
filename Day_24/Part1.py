with open("Day_24/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

lines = map(str.strip, data)

b = set()

for line in lines:
    i = iter(line)
    d = (0, 0)
    while i:
        try:
            c = next(i)
        except StopIteration:
            break
        if c == 'e':
            d = (d[0] + 1, d[1])
        if c == 'w':
            d = (d[0] - 1, d[1])
        if c in 'ns':
            c = c + next(i)
        if c == 'ne':
            d = (d[0] + 1, d[1] - 1)
        if c == 'nw':
            d = (d[0], d[1] - 1)
        if c == 'se':
            d = (d[0], d[1] + 1)
        if c == 'sw':
            d = (d[0] - 1, d[1] + 1)
    if d in b:
        b.remove(d)
    else:
        b.add(d)

# part1
print(len(b))

