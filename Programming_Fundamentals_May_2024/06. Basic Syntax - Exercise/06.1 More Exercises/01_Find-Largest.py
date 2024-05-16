num = input()

digits = []
result = ''

for d in num:
    digits.append(d)
    digits.sort()
for e in digits:
    result = e + result

print(result)
