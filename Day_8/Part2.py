with open('Day_8/input.txt', 'r') as file:
    data = file.readlines()


def test(data):
    _list = []
    accumulator = 0
    i = 0
    while i < len(data):
        line = data[i]
        if i in _list:
            break
        else:
            _list.append(i)

        line = line.split()

        if line[0] == 'acc':
            accumulator += int(line[1])
        elif line[0] == 'jmp':
            i = i + int(line[1])
            continue

        i += 1
    return (_list, accumulator, i)


def change(data, i):
    line = data[i].split()

    if line[0] == 'jmp':
        data[i] = 'nop ' + data[1]
    elif line[0] == 'nop':
        data[i] = 'jmp ' + data[1]
    else:
        return None
    return data


_list = test(data)[0]

for i in _list:
    if _data:
        = change(data, i) is None:
        continue
    if (temp: = test(_data))[0][2] == len(data) - 1:
        break

print(temp[1])
