from collections import deque

people = deque(input().split())
times = int(input())

while len(people) > 1:
    for i in range(times):
        player = people.popleft()
        if i < times - 1:
            people.append(player)
        else:
            print(f"Removed {player}")

print(f"Last is {people.popleft()}")



