with open('../Day_6/input.txt', 'r') as file:
    data = file.readlines()

answers = []
_set = set()

for line in data:
    if line.strip() == '':
        answers.append(_set)
        _set = set()
    else:
        for char in line.strip():
            _set.add(char)

_sum = 0
for _set in answers:
    _sum += len(_set)

print(_sum)
