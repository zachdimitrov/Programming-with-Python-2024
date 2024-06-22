people = list(map(int, input().split(" ")))
nxt = int(input())
executed = []
i = 0

while len(people) > 0:
    if (i + nxt - 1) < len(people):
        i = i + nxt - 1
        executed.append(people.pop(i))
    else:
        i = i - len(people)

print(str(executed).replace(" ", ""))
