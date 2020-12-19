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

rules['8'] = '42 | 42 8'
rules['9'] = '42 31 | 42 11 31'

_set = set()

while True:
    temp = False
    for num, rule in rules.items():
        if rule[0] == '"':
            _dict[num] = list(rule)[1]
        else:
            parts = rule.split(" ")
            allFound = True
            for part in parts:
                if part == "|":
                    continue

                if part not in _dict.keys():
                    allFound = False

            r = ""
            if allFound:
                for part in parts:
                    if part == "|":
                        r += "|"
                    else:
                        r = r + _dict[part]

                _dict[num] = "(" + r + ")"

    for message in messages:
        if re.fullmatch(_dict["0"], message):
            if message not in _set:
                _set.add(message)
                temp = True

    if not temp:
        print(len(_set))
        break
