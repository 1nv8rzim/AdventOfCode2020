with open("Day_16/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

fields = data[:20]
my_ticket = [int(x) for x in data[22].split(",")]
tickets = [[int(x) for x in line.split(",")] for line in data[25:]]

_dict = {}

for field in fields:
    name, rest = field.split(": ")
    rest, _rest = rest.split(" or ")
    a, b = rest.split("-")
    c, d = _rest.split("-")
    _dict[name] = [(int(a), int(b)), (int(c), int(d))]

correct = []
error = 0

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

options = [set(_dict.keys()) for _ in my_ticket]

for ticket in correct:
    for index, value in enumerate(ticket):
        for field, _range in _dict.items():
            temp = False
            for lower, upper in _range:
                if lower <= value and value <= upper:
                    temp = True
                    break
            if not temp:
                options[index].remove(field)

for i in range(len(options)):
    for j in range(len(options)):
        if len(options[j]) == 1:
            for k in range(len(options)):
                if j != k:
                    options[k] -= options[j]

num = 1

for i in range(len(my_ticket)):
    for option in options[i]:
        if option[:9] == 'departure':
            num *= my_ticket[i]

print(num)
