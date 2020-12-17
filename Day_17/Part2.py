with open("Day_17/input.txt") as file:
    data = [line.strip() for line in file.readlines()]


def _range(dim, _set):
    return range(min(_dim[dim] for _dim in _set) - 1, max(_dim[dim] for _dim in _set) + 2)


space = set()

for x, line in enumerate(data):
    for y, _char in enumerate(line):
        if _char == '#':
            space.add((x, y, 0, 0))

for _ in range(6):
    _space = set()
    for x in _range(0, space):
        for y in _range(1, space):
            for z in _range(2, space):
                for w in _range(3, space):
                    count = 0
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            for dz in (-1, 0, 1):
                                for dw in (-1, 0, 1):
                                    if not(dx == dy == dz == dw == 0):
                                        if ((x + dx, y + dy, z + dz, w + dw)) in space:
                                            count += 1
                    if (x, y, z, w) in space and count in (2, 3):
                        _space.add((x, y, z, w))
                    if (x, y, z, w) not in space and count == 3:
                        _space.add((x, y, z, w))
    space = _space

print(len(space))
