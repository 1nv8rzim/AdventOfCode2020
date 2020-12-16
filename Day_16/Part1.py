with open("Day_16/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

fields = data[:20]
your_ticket = [int(x) for x in data[22].split(",")]
tickets = [[int(x) for x in line.split(",")] for line in data[25:]]

_dict = {}

for field in fields:
    name, rest = field.split(": ")
    rest, _rest = rest.split(" or ")
    a, b = rest.split("-")
    c, d = _rest.split("-")
    _dict[name] = [(int(a), int(b)), (int(c), int(d))]

error = 0
correct = []

for ticket in tickets:
    temp = True

    for num in ticket:
        _temp = False
        for field, _range in _dict.items():
            for lower, upper in _range:
                if lower <= num and num <= upper:
                    _temp = True
                    break
            if _temp:
                break
        if not _temp:
            error += num
            temp = False

    if temp:
        correct.append(ticket)

print(error)
