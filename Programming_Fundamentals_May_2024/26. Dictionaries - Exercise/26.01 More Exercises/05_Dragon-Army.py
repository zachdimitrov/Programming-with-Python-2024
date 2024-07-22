def check_null(skill, def_skill):
    if skill == "null":
        skill = def_skill
    else:
        skill = int(skill)
    return skill


types = {}
def_health = 250
def_damage = 45
def_armor = 10

lines = int(input())

for i in range(lines):
    line = input().split(" ")
    dtype = line[0]
    dname = line[1]
    damage = check_null(line[2], def_damage)
    health = check_null(line[3], def_health)
    armor = check_null(line[4], def_armor)

    if dtype not in types:
        types[dtype] = {dname: [damage, health, armor]}
    else:
        types[dtype][dname] = [damage, health, armor]

#print(types)
for tp, dragons in types.items():
    t_damage = 0
    t_health = 0
    t_armor = 0
    for d in dragons.values():
        t_damage += d[0]
        t_armor += d[2]
        t_health += d[1]
    count = len(dragons)
    avg_damage = t_damage/count
    avg_health = t_health/count
    avg_armor = t_armor/count

    print(f"{tp}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    sorted_dragons = dict(sorted(dragons.items()))
    for name, skill in sorted_dragons.items():
        print(f"-{name} -> damage: {skill[0]}, health: {skill[1]}, armor: {skill[2]}")
