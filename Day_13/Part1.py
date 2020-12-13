with open("Day_13/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

time = int(data[0])
_ids = [int(_id) for _id in filter(lambda x: x != 'x', data[1].split(','))]
delay = [(((time // _id) + 1) * _id) - time for _id in _ids]

print(min(delay), _ids[delay.index(min(delay))],
      min(delay) * _ids[delay.index(min(delay))])
