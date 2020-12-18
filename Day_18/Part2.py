with open("Day_18/input.txt") as file:
    data = [line.strip() for line in file.readlines()]


class temp:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return temp(self.value + other.value)

    def __sub__(self, other):
        return temp(self.value * other.value)

    def __mul__(self, other):
        return temp(self.value + other.value)


_sum = 0
for line in data:
    for i in range(10):
        line = line.replace(f"{i}", f"temp({i})")
    line = line.replace("*", "-").replace("+", "*")
    _sum += eval(line, {"temp": temp}).value
print(_sum)
