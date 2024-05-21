lines = int(input())
capacity = 255
filled = 0
for i in range(0, lines):
    liters = int(input())
    if filled + liters > capacity:
        print('Insufficient capacity!')
    else:
        filled += liters
print(filled)
