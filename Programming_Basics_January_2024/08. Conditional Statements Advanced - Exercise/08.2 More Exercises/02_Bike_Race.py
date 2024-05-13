juniors = int(input())
seniors = int(input())
race_type = input()

money = 0

if race_type == 'trail':
    money = juniors * 5.5 + seniors * 7
elif race_type == 'cross-country':
    money = juniors * 8 + seniors * 9.5
    if juniors + seniors >= 50:
        money -= money * 0.25
elif race_type == 'downhill':
    money = juniors * 12.25 + seniors * 13.75
elif race_type == 'road':
    money = juniors * 20 + seniors * 21.5

money -= money * 0.05

print(f'{money:.2f}')
