city = input()
if city != 'Bansko' and city != 'Borovets' and city != 'Varna' and city != 'Burgas':
    print('Invalid input!')
    exit()
package = input()

if package != 'withEquipment' and package != 'noEquipment' and package != 'withBreakfast' and package != 'noBreakfast':
    print('Invalid input!')
    exit()
vip = input()

if vip != 'yes' and vip != 'no':
    print('Invalid input!')
    exit()

days = int(input())

if days < 1:
    print('Days must be positive number!')
    exit()
if days > 7:
    days = days - 1

price = 0

if city == 'Bansko' or city == 'Borovets':
    if package == 'withEquipment':
        price = 100
        if vip == 'yes':
            price = price - price * 0.1
    elif package == 'noEquipment':
        price = 80
        if vip == 'yes':
            price = price - price * 0.05
elif city == 'Varna' or city == 'Burgas':
    if package == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price = price - price * 0.12
    elif package == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price = price - price * 0.7

print(f'The price is {days * price:.2f}lv! Have a nice time!')

