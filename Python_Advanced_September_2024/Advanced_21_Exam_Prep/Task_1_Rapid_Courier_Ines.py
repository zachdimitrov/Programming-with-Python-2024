from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])
total_delivered = 0

while packages and couriers:
    current_package = packages[-1]
    current_courier = couriers[0]
    if current_courier >= current_package:
        capacity = current_courier - current_package * 2
        couriers.popleft()
        if capacity > 0:
            couriers.append(capacity)
        total_delivered += packages.pop()

