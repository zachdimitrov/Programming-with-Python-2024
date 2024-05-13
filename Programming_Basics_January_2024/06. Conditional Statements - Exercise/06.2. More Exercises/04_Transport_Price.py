distance = int(input())
time_of_day = input()
price = 0

if distance < 20:
    price = 0.7 + (0.79 * distance if time_of_day == 'day' else 0.9 * distance)
elif 20 <= distance < 100:
    price = 0.09 * distance
else:
    price = 0.06 * distance

print(f'{price:.2f}')
