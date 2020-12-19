import re

with open("Day_19/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

rules = {}
for line in data[:132]:
    line = line.split(': ')
    rules[line[0]] = line[1]

messages = data[133:]

_dict = {}

while '0' not in _dict.keys():
    for num, rule in rules.items():
        if rule[0] == '"':
            _dict[num] = list(rule)[1]
        else:
            rule = rule.split()
            temp = True
            for _rule in rule:
                if _rule == '|':
                    continue
                if _rule not in _dict.keys():
                    temp = False

            _result = ''
            if temp:
                for _rule in rule:
                    if _rule == '|':
                        _result += _rule
                    else:
                        _result += _dict[_rule]

                _dict[num] = f'({_result})'

matches = 0
for messages in messages:
    if re.fullmatch(_dict['0'], messages):
        matches += 1

print(matches)
