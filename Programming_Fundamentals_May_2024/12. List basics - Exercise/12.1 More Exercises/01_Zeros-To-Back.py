read = input().split(", ")
initial = list(map(int, read))
zeros = 0

for i in range(len(initial) - 1, -1, -1):
    if initial[i] == 0:
        initial.pop(i)
        zeros += 1

for j in range(zeros):
    initial.append(0)

print(initial)
