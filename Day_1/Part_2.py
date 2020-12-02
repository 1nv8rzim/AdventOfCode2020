with open('Day 1/input.txt', 'r') as input:
    data = [int(line.strip()) for line in input]

for index_i, i in enumerate(data):
    for index_j, j in enumerate(data[index_i+1:]):
        for k in data[index_j+1:]:
            if i + j + k == 2020:
                print(i, j, k, i*j*k)
