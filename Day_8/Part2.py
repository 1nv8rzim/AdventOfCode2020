with open('Day_8/input.txt', 'r') as file:
    x = file.readlines()


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
            accumulator += int(line[-1])
        elif line[0] == 'jmp':
            i = i + int(line[-1])
            continue

        i += 1
    return (_list, accumulator, i)


def change(data, i):
    _data = data[:]
    line = _data[i].strip().split()
    if _data[i][:3] == 'jmp':
        _data[i] = 'nop' + _data[i][3:]
    elif _data[i][:3] == 'nop':
        _data[i] = 'jmp' + _data[i][3:]
    else:
        return None
    return _data


_list = test(x)[0]

for i in _list:
    _data = change(x, i)
    if _data is None:
        continue
    temp = test(_data)
    if temp[2] == len(x):
        print(temp[1])
        break
