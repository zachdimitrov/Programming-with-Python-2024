group = int(input())
days = int(input())
all_coins = 0
for i in range(1, days + 1):
    all_coins += 50
    if i % 10 == 0:
        group -= 2
    if i % 15 == 0:
        group += 5
    all_coins -= group * 2
    if i % 3 == 0:
        all_coins -= group * 3
    if i % 5 == 0:
        all_coins += group * 20
    if i % 15 == 0:
        all_coins -= group * 2

print(f'{group} companions received {int(all_coins / group)} coins each.')
