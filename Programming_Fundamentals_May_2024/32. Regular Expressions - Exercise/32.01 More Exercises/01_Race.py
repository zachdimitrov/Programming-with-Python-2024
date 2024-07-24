import re
in_names = input().split(", ")
line = input()
pattern1 = r"([A-Za-z])"
pattern2 = r"([\d])"
racers = {}
while line != "end of race":
    names = re.findall(pattern1, line)
    dists = re.findall(pattern2, line)
    name = "".join(names)
    dist = 0
    for d in dists:
        dist += int(d)
    if name in in_names:
        if name not in racers:
            racers[name] = dist
        else:
            racers[name] += dist
    line = input()

sorted_racers = dict(sorted(racers.items(), key=lambda x: x[1], reverse=True))
keys = list(sorted_racers.keys())
print(f"1st place: {keys[0]}")
print(f"2nd place: {keys[1]}")
print(f"3rd place: {keys[2]}")
