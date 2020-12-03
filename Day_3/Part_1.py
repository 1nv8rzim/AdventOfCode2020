with open('Day_3/input.txt', 'r') as file:
    data = file.readlines()


def count_trees(area, x_step, y_step):
    x = y = trees = 0
    while y < len(area):
        if area[y][x] == '#':
            trees -= -1
        x, y = (x + x_step) % (len(area[y]) - 1), y + y_step
    return trees


print(count_trees(data, 3, 1))
