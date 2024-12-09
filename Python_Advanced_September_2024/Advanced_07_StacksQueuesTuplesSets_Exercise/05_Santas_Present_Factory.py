from collections import deque

materials = [int(n) for n in input().split()]   # stack
magic = deque([int(n) for n in input().split()])  # queue
presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted = {}
success = False

while materials and magic:
    current_mat = materials.pop()
    current_magic = magic.popleft()
    if current_mat == 0:
        if current_magic != 0:
            magic.appendleft(current_magic)
        continue
    if current_magic == 0:
        if current_mat != 0:
            materials.append(current_mat)
        continue

    total_magic = current_magic * current_mat

    if total_magic in presents.keys():
        if presents[total_magic] not in crafted:
            crafted[presents[total_magic]] = 1
        else:
            crafted[presents[total_magic]] += 1
    else:
        if total_magic > 0:
            current_mat += 15
            materials.append(current_mat)
        else:
            result = current_mat + current_magic
            materials.append(result)
    if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" in crafted and "Bicycle" in crafted):
        success = True

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(a) for a in materials][::-1])}")
if magic:
    print(f"Magic left: {', '.join([str(a) for a in magic])}")
if crafted:
    ordered_crafted = dict(sorted(crafted.items()))
    for key, value in ordered_crafted.items():
        print(f"{key}: {value}")

