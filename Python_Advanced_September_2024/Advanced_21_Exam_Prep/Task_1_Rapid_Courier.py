from collections import deque

weights = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])

delivered = 0
while weights and couriers:
    next_weight = weights.pop()
    next_courier = couriers.popleft()

    if next_courier >= next_weight:
        delivered += next_weight
        next_courier -= 2 * next_weight
        if next_courier > 0:
            couriers.append(next_courier)
    else:
        delivered = delivered + next_courier
        weights.append(next_weight - next_courier)

print(f"Total weight: {delivered} kg")
if len(couriers) == 0 and len(weights) == 0:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif len(couriers) == 0 and len(weights) > 0:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join([str(x) for x in weights])}")
elif len(couriers) > 0 and len(weights) == 0:
    print(f"Couriers are still on duty: "
          f"{', '.join([str(x) for x in couriers])} "
          f"but there are no more packages to deliver.")
