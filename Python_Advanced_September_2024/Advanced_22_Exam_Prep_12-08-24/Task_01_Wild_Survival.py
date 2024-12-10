from collections import deque

bee_groups = deque([int(x) for x in input().split()])
bee_eaters = [int(x) for x in input().split()]

while bee_groups and bee_eaters:
    last_eaters = bee_eaters.pop()
    first_bees = bee_groups.popleft()
    while True:
        if first_bees <= 0 or last_eaters <= 0:
            break
        if first_bees >= 7:
            last_eaters -= 1
            first_bees -= 7
        else:
            first_bees = 0
    if last_eaters > 0:
        bee_eaters.append(last_eaters)
    if first_bees > 0:
        bee_groups.append(first_bees)

print("The final battle is over!")
if len(bee_groups) == 0 and len(bee_eaters) == 0:
    print("But no one made it out alive!")
if len(bee_groups) > 0:
    print(f"Bee groups left: {', '.join([str(x) for x in bee_groups])}")
if len(bee_eaters) > 0:
    print(f"Bee-eater groups left: {', '.join([str(x) for x in bee_eaters])}")
