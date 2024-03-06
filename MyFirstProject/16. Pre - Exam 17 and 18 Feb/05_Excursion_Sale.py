sea_vacations = int(input())
mount_vacations = int(input())

profit = 0

while True:
    command = input()
    if command == 'Stop':
        break
    if command == 'sea':
        if sea_vacations > 0:
            profit += 680
            sea_vacations -= 1
        else:
            continue
    if command == 'mountain':
        if mount_vacations > 0:
            profit += 499
            mount_vacations -= 1
        else:
            continue
    if mount_vacations == 0 and sea_vacations == 0:
        break

if mount_vacations == 0 and sea_vacations == 0:
    print('Good job! Everything is sold.')
print(f'Profit: {profit} leva.')
