with open('Day_10/input.txt', 'r') as file:
    data = file.readlines()

for index, num in enumerate(data):
    data[index] = int(num.strip())

data = sorted(data)

diff = [0, 0, 0]
jolt = 0

for num in data:
    if num - jolt == 1:
        print(1, num, jolt)
        diff[0] += 1
        jolt = num
    elif num - jolt == 2:
        diff[1] += 1
        jolt = num
    elif num - jolt == 3:
        print(3, num, jolt)
        diff[2] += 1
        jolt = num
    elif num == jolt:
        continue
    else:
        print('Failure:', num, jolt)

print(diff[0], diff[2], diff[0] * (diff[2] + 1))
