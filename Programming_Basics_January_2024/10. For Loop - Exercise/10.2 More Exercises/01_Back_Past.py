money = float(input())
year = int(input())

for i in range(1800, year + 1):
    if i % 2 == 0:
        money = money - 12000
    else:
        money = money - 12000 - 50 * (18 + i - 1800)

if money < 0:
    print(f'He will need {abs(money):.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
