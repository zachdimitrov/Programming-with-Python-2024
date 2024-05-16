word = input()
capitals = []
i = 0
for c in word:
    if 65 <= ord(c) <= 90:
        capitals.append(i)
    i += 1

print(capitals)
