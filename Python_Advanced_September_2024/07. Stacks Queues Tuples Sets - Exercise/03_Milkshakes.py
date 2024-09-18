from collections import deque

chocolates = [int(n) for n in input().split(", ")]   # stack
milk = deque([int(n) for n in input().split(", ")])  # queue
shakes = 0

while chocolates and milk and shakes < 5:
    chocolate = chocolates.pop()
    cup = milk.popleft()
    if chocolate <= 0:
        if cup > 0:
            milk.appendleft(cup)
        continue
    if cup <= 0:
        if chocolate > 0:
            chocolates.append(chocolate)
        continue
    if cup == chocolate:
        shakes += 1
    else:
        chocolate -= 5
        chocolates.append(chocolate)
        milk.append(cup)

if shakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(a) for a in chocolates])}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join([str(a) for a in milk])}")
else:
    print("Milk: empty")
