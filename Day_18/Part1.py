with open("Day_18/input.txt") as file:
    data = [line.strip() for line in file.readlines()]


def parse(expr):
    expr = expr.replace(' ', '')

    def _helper(iter):
        items = []
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError(
                        "bad expression -- unbalanced parentheses")
                items.append(result)
            elif item == ')':
                return items, True
            else:
                items.append(item)
        return items, False
    return _helper(iter(expr))[0]


def math(_line):
    num1 = _line[0]
    if isinstance(num1, list):
        num1 = math(num1)

    operator = _line[1]
    num2 = _line[2]

    if isinstance(num2, list):
        num2 = math(num2)
    num2 = num2

    result = str(eval(num1 + operator + num2))
    if len(_line) == 3:
        return result

    _line = [result] + _line[3:]
    return math(_line)


def parse_expression(_line):
    return math(parse(_line))


_sum = 0

for line in data:
    _sum += int(parse_expression(line))

print(_sum)
