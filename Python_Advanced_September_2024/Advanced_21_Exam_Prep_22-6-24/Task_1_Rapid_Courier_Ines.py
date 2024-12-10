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
    else:
        packages[-1] -= couriers.popleft()
        total_delivered += current_courier

print(f"Total weight: {total_delivered} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
if packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: ")


