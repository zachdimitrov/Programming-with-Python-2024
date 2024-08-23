from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))
next_order = 0
completed = True

while len(orders):
    next_order = orders.popleft()
    if food >= next_order:
        food -= next_order
    else:
        completed = False
        break

if len(orders):
    print("Orders left:", end=" ")
    print(next_order, end=" ")
    while len(orders):
        print(orders.popleft(), end=" ")
else:
    if not completed:
        print(f"Orders left: {next_order}")
    else:
        print("Orders complete")
