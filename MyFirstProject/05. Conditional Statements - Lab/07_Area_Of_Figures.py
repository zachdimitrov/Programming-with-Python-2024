from math import pi

figure = input()
result = 0.0
if figure == 'square':
    side = float(input())
    result = side * side
elif figure == 'rectangle':
    length = float(input())
    height = float(input())
    result = length * height
elif figure == 'circle':
    radius = float(input())
    result = pi * radius * radius
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    result = 0.5 * height * side

print(f'{result:.3f}')
