from collections import deque

bees = deque([int(n) for n in input().split()])  # queue
nectar = [int(n) for n in input().split()]   # stack
symbols = deque(input().split())
result = 0

while bees and nectar:
    next_bee = bees.popleft()
    next_nectar = nectar.pop()

    if next_nectar >= next_bee:
        symbol = symbols.popleft()
        if symbol == "+":
            result = result + next_bee + next_nectar
        elif symbol == "-":
            result = result + abs(next_bee - next_nectar)
        elif symbol == "*":
            result = result + next_bee * next_nectar
        elif symbol == "/":
            if next_nectar != 0:
                result = result + next_bee / next_nectar
    else:
        bees.appendleft(next_bee)

print(f"Total honey made: {result}")
if bees:
    print(f"Bees left: {', '.join([str(a) for a in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(a) for a in nectar])}")
