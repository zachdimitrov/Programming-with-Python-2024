num = int(input())
names = set()
for _ in range(num):
    names.add(input())
print(*names, sep="\n")

