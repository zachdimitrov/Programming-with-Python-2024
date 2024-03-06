days = int(input())
hours = int(input())
total_sum = 0

for i in range(1, days + 1):
    days_sum = 0
    for j in range(1, hours + 1):
        if i % 2 == 0:
            if j % 2 != 0:
                days_sum += 2.5
            else:
                days_sum += 1
        else:
            if j % 2 == 0:
                days_sum += 1.25
            else:
                days_sum += 1
    print(f'Day: {i} - {days_sum:.2f} leva')
    total_sum += days_sum
print(f'Total: {total_sum:.2f} leva')
