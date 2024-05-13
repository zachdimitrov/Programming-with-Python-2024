n = int(input())
found = False

for a in range(1, 10):
    if found:
        break
    for b in range(9, a - 1, -1):
        if found:
            break
        for c in range(0, 10):
            if found:
                break
            for d in range(9, a - 1, -1):
                if a + b + c + d == a * b * c * d and n % 10 == 5:
                    print(str(a) + str(b) + str(c) + str(d))
                    found = True
                    break
                elif a * b * c * d // (a + b + c + d) == 3 and n % 3 == 0:
                    print(str(d) + str(c) + str(b) + str(a))
                    found = True
                    break

if not found:
    print('Nothing found')
