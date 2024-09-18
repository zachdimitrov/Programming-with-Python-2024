from collections import deque

line = deque(input().split())
result = 0
current_numbers = deque()
start = True
first_number = 0

while line:
    symbol = line.popleft()
    if symbol[-1].isdigit():
        current_numbers.append(int(symbol))
    else:
        if start:
            first_number = current_numbers.popleft()
            start = False
        while current_numbers:
            next_number = current_numbers.popleft()
            if symbol == "*":
                result = first_number * next_number
            elif symbol == "+":
                result = first_number + next_number
            elif symbol == "-":
                result = first_number - next_number
            elif symbol == "/":
                result = first_number // next_number
            first_number = result

print(result)
