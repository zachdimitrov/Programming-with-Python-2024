change = int(float(input()) * 100)
coins = 0
two_lv = 0
one_lv = 0
fifty = 0
twenty = 0
ten = 0
five = 0
two = 0
one = 0

while change > 0:
    if change >= 200:
        coins += 1
        two_lv += 1
        change = change - 200
    elif 100 <= change < 200:
        coins += 1
        one_lv += 1
        change = change - 100
    elif 50 <= change < 100:
        coins += 1
        fifty += 1
        change = change - 50
    elif 20 <= change < 50:
        coins += 1
        twenty += 1
        change = change - 20
    elif 10 <= change < 20:
        coins += 1
        ten += 1
        change = change - 10
    elif 5 <= change < 10:
        coins += 1
        five += 1
        change = change - 5
    elif 2 <= change < 5:
        coins += 1
        two += 1
        change = change - 2
    elif 1 <= change < 2:
        coins += 1
        one += 1
        change = change - 1

print(f'Number of coins: {coins}')
print('----------------------')
print(f'2 lv: {two_lv}')
print(f'1 lv: {one_lv}')
print(f'0.5 lv: {fifty}')
print(f'0.2 lv: {twenty}')
print(f'0.1 lv: {ten}')
print(f'0.05 lv: {five}')
print(f'0.02 lv: {two}')
print(f'0.01 lv: {one}')

