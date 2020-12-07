with open('Day_7/input.txt', 'r') as file:
    data = file.readlines()

_dict = {'other': []}

for line in data:
    line = line.strip()[:-1].split(' bags contain ')
    _dict[line[0]] = tuple(_line.rsplit(' ', 1)[0].strip().split(' ', 1)[1]
                           for _line in line[1].split(','))


def check_shiny_gold(bag):
    if bag == 'other':
        return False
    if 'shiny gold' in _dict[bag]:
        return True
    return any(check_shiny_gold(_bag) for _bag in _dict[bag])


counter = 0

for element in _dict:
    if check_shiny_gold(element):
        counter += 1

print(counter)
