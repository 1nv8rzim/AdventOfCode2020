import re

with open('Day_4/input.txt', 'r') as file:
    data = file.readlines()

passports = ['']
needed = {'byr':range(1920,2003), 'iyr':range(2010,2021), 'eyr':range(2020,2031), 'hgt':{'in':range(59,77),'cm':range(150,194)}, 'hcl':re.compile('^#[0-9a-f]{6}$'), 'ecl':('amb', 'blu', 'gry', 'grn', 'hzl', 'oth'),'pid':re.compile('^[0-9]{9}$')}
counter = 0

for line in data:
    if line.strip() == '':
        counter += 1
        passports.append('')
    else:
        passports[counter] += line.strip() + ' '

for index, line in enumerate(passports):
    _dict = {}
    for attr in line.split():
        split = attr.split(':')
        _dict[split[0]] = split[1]
    passports[index] = _dict

#for line in passports:
    #print(line)

counter = 0

for passport in passports:
    _pass = True
    for field in needed:
        if field not in passport:
            _pass = False
            continue
        if field == 'pid' or field == 'hcl':
            if not needed[field].match(passport[field]):
                _pass = False
        elif field == 'hgt':
            if passport[field][-2:] == 'cm':
                try:
                    if not int(passport[field][:-2]) in passport[field]['cm']:
                        _pass = False
                except:
                    _pass = False
            elif passport[field][-2:] == 'cm':
                try:
                    if not int(passport[field][:-2]) in passport[field]['in']:
                        _pass = False
                except:
                    _pass = False
            else:
                _pass = False
        elif field == 'ecl':
            if passport[field] not in needed[field]:
                _pass = False
        else:
            if passport[field] not in needed[field]:
                _pass = False
    counter += 1 if _pass else 0

print(counter)
