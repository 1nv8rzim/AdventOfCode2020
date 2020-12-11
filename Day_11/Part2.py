import copy

with open("Day_11/input.txt") as file:
    data = [list(line.strip()) for line in file.readlines()]


num_steps = 0
while True:
    num_steps += 1
    temp = True
    new = copy.deepcopy(data)
    for j in range(0, len(data)):
        for i in range(0, len(data[j])):
            adj = []
            jj = j
            while True:
                jj += 1
                if jj >= len(data):
                    break
                if data[jj][i] in ["#", "L"]:
                    adj.append(data[jj][i])
                    break
            jj = j
            while True:
                jj -= 1
                if jj < 0:
                    break
                if data[jj][i] in ["#", "L"]:
                    adj.append(data[jj][i])
                    break
            ii = i
            while True:
                ii += 1
                if ii >= len(data[j]):
                    break
                if data[j][ii] in ["#", "L"]:
                    adj.append(data[j][ii])
                    break
            ii = i
            while True:
                ii -= 1
                if ii < 0:
                    break
                if data[j][ii] in ["#", "L"]:
                    adj.append(data[j][ii])
                    break
            ii = i
            jj = j
            while True:
                ii += 1
                jj += 1
                if ii >= len(data[j]) or jj >= len(data):
                    break
                if data[jj][ii] in ["#", "L"]:
                    adj.append(data[jj][ii])
                    break
            ii = i
            jj = j
            while True:
                ii -= 1
                jj += 1
                if ii < 0 or jj >= len(data):
                    break
                if data[jj][ii] in ["#", "L"]:
                    adj.append(data[jj][ii])
                    break
            ii = i
            jj = j
            while True:
                ii -= 1
                jj -= 1
                if ii < 0 or jj < 0:
                    break
                if data[jj][ii] in ["#", "L"]:
                    adj.append(data[jj][ii])
                    break
            ii = i
            jj = j
            while True:
                ii += 1
                jj -= 1
                if ii >= len(data[j]) or jj < 0:
                    break
                if data[jj][ii] in ["#", "L"]:
                    adj.append(data[jj][ii])
                    break
            occupied_adj = adj.count("#")
            if data[j][i] == "L" and occupied_adj == 0:
                new[j][i] = "#"
                temp = False
            elif data[j][i] == "#" and occupied_adj >= 5:
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
