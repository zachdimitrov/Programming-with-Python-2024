from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]

wasted_water = 0
current_cup = cups.popleft()

while bottles:
    bottle = bottles.pop()
    if bottle >= current_cup:
        wasted_water = wasted_water + (bottle - current_cup)
        if cups and bottles:
            current_cup = cups.popleft()
        else:
            break
    else:
        current_cup -= bottle

if not cups:
    print(f"Bottles: {' '.join([str(el) for el in bottles])}")
else:
    print(f"Cups: {' '.join([str(el) for el in cups])}")
print(f"Wasted litters of water: {wasted_water}")
