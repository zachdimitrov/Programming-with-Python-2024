first = set()
for el in [int(a) for a in input().split()]:
    first.add(el)
second = set()
for el in [int(a) for a in input().split()]:
    second.add(el)
n = int(input())

for _ in range(n):
    commands = input().split()
    numbers = []
    if commands[0] == "Check":
        print(first.issubset(second) or second.issubset(first))
    else:
        numbers = [int(x) for x in commands[2:]]

    if commands[0] == "Add":
        for n in numbers:
            if commands[1] == "First":
                first.add(n)
            else:
                second.add(n)
    elif commands[0] == "Remove":
        for n in numbers:
            if commands[1] == "First":
                if n in first:
                    first.remove(n)
            else:
                if n in second:
                    second.remove(n)

print(f"{', '.join([str(s) for s in sorted([a for a in first])])}")
print(f"{', '.join([str(s) for s in sorted([a for a in second])])}")
