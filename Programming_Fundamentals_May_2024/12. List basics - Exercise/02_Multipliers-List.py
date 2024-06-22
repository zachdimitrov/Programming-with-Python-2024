factor = int(input())
num = int(input())
multipliers = []

for i in range(1, num + 1):
    multipliers.append(factor * i)

print(multipliers)
