with open('../Day_6/input.txt', 'r') as file:
    data = file.readlines()

answers = []
_list = []

for line in data:
    if line.strip() == '':
        temp = set.intersection(*_list)
        if len(temp):
            answers.append(temp)
        _list = []
    else:
        _set = set()
        for char in line.strip():
            _set.add(char)
        _list.append(_set)

_sum = 0
for _set in answers:
    _sum += len(_set)

for line in answers:
    print(line)

print(_sum)
