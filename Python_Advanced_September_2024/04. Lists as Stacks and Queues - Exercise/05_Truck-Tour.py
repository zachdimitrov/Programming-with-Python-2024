from collections import deque

n = int(input())
pumps = deque()
for i in range(n):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

station = 0
fuel = 0

# visited = 0

# while visited < n - 1:
#     current = pumps.popleft()
#     if current[0] + fuel < current[1]:
#         station += 1
#         visited = 0
#         fuel = 0
#     else:
#         fuel += current[0]
#         fuel -= current[1]
#         visited += 1
#     pumps.append(current)

for i in range(n):
    current = pumps.popleft()
    fuel = fuel + current[0] - current[1]
    if fuel < 0:
        fuel = 0
        station = i + 1

print(station)
