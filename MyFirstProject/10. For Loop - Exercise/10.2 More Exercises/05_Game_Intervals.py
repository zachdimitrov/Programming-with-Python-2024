turns = int(input())

interval_0_9 = 0
interval_10_19 = 0
interval_20_29 = 0
interval_30_39 = 0
interval_40_50 = 0
invalid = 0
points = 0

for i in range(0, turns):
    number = int(input())
    if 0 <= number <= 9:
        interval_0_9 += 1
        points += number * 0.2
    elif 10 <= number <= 19:
        interval_10_19 += 1
        points += number * 0.3
    elif 20 <= number <= 29:
        interval_20_29 += 1
        points += number * 0.4
    elif 30 <= number <= 39:
        interval_30_39 += 1
        points += 50
    elif 40 <= number <= 50:
        interval_40_50 += 1
        points += 100
    else:
        invalid += 1
        points *= 0.5

print(f'{points:.2f}')
print(f'From 0 to 9: {interval_0_9 / turns * 100:.2f}%')
print(f'From 10 to 19: {interval_10_19 / turns * 100:.2f}%')
print(f'From 20 to 29: {interval_20_29 / turns * 100:.2f}%')
print(f'From 30 to 39: {interval_30_39 / turns * 100:.2f}%')
print(f'From 40 to 50: {interval_40_50 / turns * 100:.2f}%')
print(f'Invalid numbers: {invalid / turns * 100:.2f}%')
