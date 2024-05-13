from math import floor, ceil
magnolia = int(input())
zumbul = int(input())
rose = int(input())
cactus = int(input())
gift_price = float(input())

money_earned = magnolia * 3.25 + zumbul * 4 + rose * 3.5 + cactus * 8
money_earned = money_earned - 0.05 * money_earned

if money_earned >= gift_price:
    print(f'She is left with {floor(money_earned - gift_price)} leva.')
else:
    print(f'She will have to borrow {ceil(gift_price - money_earned)} leva.')

