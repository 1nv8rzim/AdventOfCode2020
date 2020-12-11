import copy

with open("Day_11/input.txt") as file:
    data = [list(line.strip()) for line in file.readlines()]


while True:
    temp = True
    new = copy.deepcopy(data)
    for j in range(0, len(data)):
        for i in range(0, len(data[j])):
            adj = []
            if i != 0:
                adj.append(data[j][i-1])
            if i != len(data[j])-1:
                adj.append(data[j][i+1])
            if j != 0:
                adj.append(data[j-1][i])
            if j != len(data)-1:
                adj.append(data[j+1][i])
            if i != 0 and j != 0:
                adj.append(data[j-1][i-1])
            if i != len(data[j])-1 and j != len(data)-1:
                adj.append(data[j+1][i+1])
            if i != 0 and j != len(data)-1:
                adj.append(data[j+1][i-1])
            if i != len(data[j])-1 and j != 0:
                adj.append(data[j-1][i+1])
            occupied_adj = adj.count("#")
            if data[j][i] == "L" and occupied_adj == 0:
                new[j][i] = "#"
                temp = False
            elif data[j][i] == "#" and occupied_adj >= 4:
                new[j][i] = "L"
                temp = False
    if temp == True:
        sm = 0
        for j in range(0, len(data)):
            for i in range(0, len(data[j])):
                if data[j][i] == "#":
                    sm += 1
        print(sm)
        break
    data = new
