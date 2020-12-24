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


n = [(1, 0), (-1, 0), (1, -1), (0, -1), (0, 1), (-1, 1)]

def conway(b):
    c = set()
    for B in b:
        for N in n:
            c.add((B[0] + N[0], B[1] + N[1]))
    nb = set()
    for C in c:
        neighbors = 0
        for N in n:
            m = (C[0] + N[0], C[1] + N[1])
            if m in b:
                neighbors += 1
        if C in b:
            if 0 < neighbors <= 2:
                nb.add(C)
        if C not in b:
            if neighbors == 2:
                nb.add(C)
    return nb

for _ in range(100):
    b = conway(b.copy())

print(len(b))