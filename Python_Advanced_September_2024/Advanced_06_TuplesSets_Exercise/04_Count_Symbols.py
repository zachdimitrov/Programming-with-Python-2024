line = input()
occurs = {}

for c in line:
    if c not in occurs:
        occurs[c] = 1
    else:
        occurs[c] += 1

myKeys = list(occurs.keys())
myKeys.sort()
sorted_occurs = {i: occurs[i] for i in myKeys}

for ch, times in sorted_occurs.items():
    print(f"{ch}: {times} time/s")


