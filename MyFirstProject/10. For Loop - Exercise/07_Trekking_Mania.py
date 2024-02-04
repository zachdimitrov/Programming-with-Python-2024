n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
people = 0

for i in range(0, n):
    number = int(input())
    people += number
    if number <= 5:
        p1 += number
    elif 6 <= number <= 12:
        p2 += number
    elif 13 <= number <= 25:
        p3 += number
    elif 26 <= number <= 40:
        p4 += number
    elif 41 <= number:
        p5 += number

print(f'{p1 / people * 100:.2f}%')
print(f'{p2 / people * 100:.2f}%')
print(f'{p3 / people * 100:.2f}%')
print(f'{p4 / people * 100:.2f}%')
print(f'{p5 / people * 100:.2f}%')
