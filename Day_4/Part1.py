with open('Day_4/input.txt', 'r') as file:
    data = file.readlines()

passports = ['']
needed = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid')
counter = 0
for line in data:
    if line.strip() == '':
        counter += 1
        passports.append('')
    else:
        passports[counter] += line.strip() + ' '

counter = 0

for passport in passports:
    _pass = True
    for field in needed:
        if field not in passport:
            _pass = False
    counter += 1 if _pass else 0

print(counter)
