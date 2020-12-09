with open('Day_9/input.txt', 'r') as file:
    data = file.readlines()

for index, num in enumerate(data):
    data[index] = int(num.strip())

num = 32321523

for i_index, i in enumerate(data):
    for j_index, j in enumerate(data[i_index:]):
        if sum(data[i_index:j_index + 1]) == num:
            print(min(data[i_index:j_index + 1]), max(data[i_index:j_index + 1]),
                  min(data[i_index:j_index + 1]) + max(data[i_index:j_index + 1]))
