txt = input()
suma = 0
for char in txt:
    if char == 'a':
        suma+= 1
    elif char == 'e':
        suma += 2
    elif char == 'i':
        suma += 3
    elif char == 'o':
        suma += 4
    elif char == 'u':
        suma += 5

print(suma)
