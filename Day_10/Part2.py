with open('Day_10/input.txt', 'temp') as file:
    data = file.readlines()

for index, num in enumerate(data):
    data[index] = int(num.strip())

jolts = sorted(data)
combos = {}


def test(jolts, prev=0):
    if jolts == []:
        return 0
    if len(jolts) == 1:
        return 1

    num = jolts[0]
    if num in combos:
        return combos[num]

    if len(jolts) > 2 and jolts[2] <= prev + 3:
        temp = test(jolts[1:], num) + \
            test(jolts[2:], num) + test(jolts[3:], num)
        combos[num] = temp
        return temp
    if len(jolts) > 1 and jolts[1] <= prev + 3:
        temp = test(jolts[1:], num) + test(jolts[2:], num)
        combos[num] = temp
        return temp

    temp = test(jolts[1:], num)
    combos[num] = temp
    return temp


print(test(jolts + [max(jolts) + 3]))
