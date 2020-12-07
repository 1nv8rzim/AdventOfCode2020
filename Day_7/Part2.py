with open('Day_7/input.txt', 'r') as file:
    data = file.readlines()

_dict = {'other': []}

for line in data:
    line = line.strip()[:-1].split(' bags contain ')
    _dict[line[0]] = tuple(_line.rsplit(' ', 1)[0].strip()
                           for _line in line[1].split(','))


def bag_count(bag):
    bags = 1
    for _bag in _dict[bag.split(' ', 1)[1]]:
        num = _bag.split(' ', 1)[0]
        num = int(num) if num != 'no' else 0
        if num:
            bags += num * bag_count(_bag)
    return bags


print(bag_count('1 shiny gold') - 1)
