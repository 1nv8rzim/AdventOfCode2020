with open("Day_15/input.txt") as file:
    data = [line.strip() for line in file.readlines()]

data = [int(_num) for _num in data[0].split(',')]

nums = {}
previous = -1


def populate(_dict, index, num):
    if num not in _dict:
        _dict[num] = (-1, index)
    else:
        _dict[num] = (_dict[num][1], index)
    return num


for i in range(30000000):
    if i < len(data):
        previous = populate(nums, i, data[i])
        continue
    if nums[previous][0] == -1:
        previous = populate(nums, i, 0)
    else:
        previous = populate(nums, i, nums[previous][1] - nums[previous][0])

print(previous)
