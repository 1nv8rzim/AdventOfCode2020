with open('Day_9/input.txt', 'r') as file:
    data = file.readlines()

for index, num in enumerate(data):
    data[index] = int(num.strip())


def checksum(_list, num):
    for index, i in enumerate(_list):
        for j in _list[index:]:
            if i + j == num:
                return True
    return False


for index, num in enumerate(data):
    if index <= 24:
        continue
    if not checksum(data[index - 25:index], num):
        print(num)
