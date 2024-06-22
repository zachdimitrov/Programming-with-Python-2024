op = input()
ft = int(input())
sd = int(input())


def calculate(first, second, operator):
    if operator == "multiply":
        return first * second
    elif operator == "divide":
        return first / second
    elif operator == "add":
        return first + second
    elif operator == "subtract":
        return first - second


print(f'{calculate(ft, sd, op):.0f}')

