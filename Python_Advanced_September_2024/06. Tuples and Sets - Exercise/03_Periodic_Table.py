num = int(input())

elements = set()

for _ in range(num):
    els = input().split()
    for e in els:
        elements.add(e)

print(*elements, sep="\n")
