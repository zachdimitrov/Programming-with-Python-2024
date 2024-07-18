key_materials = {"shards": 0, "fragments": 0, "motes": 0}
collected = False
while True:
    line = input().split(" ")
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()

        if material not in key_materials:
            key_materials[material] = quantity
        else:
            key_materials[material] += quantity

        if key_materials[material] >= 250:
            if material == "shards":
                print("Shadowmourne obtained!")
            elif material == "fragments":
                print("Valanyr obtained!")
            elif material == "motes":
                print("Dragonwrath obtained!")
            key_materials[material] -= 250
            collected = True
            break

    if collected:
        break

'''
shard = key_materials.pop("shards")
print(f"{shard[0]}: {shard[1]}")
fragment = key_materials.pop("fragments")
print(f"{fragment[0]}: {fragment[1]}")
mote = key_materials.pop("motes")
print(f"{mote[0]}: {mote[1]}")
'''
for key, value in key_materials.items():
    print(f"{key}: {value}")
