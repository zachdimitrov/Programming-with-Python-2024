hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price = 0


def calculate_price(s):
    final = 0
    if s == 'Spring' or s == 'Summer':
        final += hrizantemi * 2
        final += roses * 4.1
        final += tulips * 2.5
        if holiday == 'Y':
            final += final * 0.15
    elif s == 'Autumn' or s == 'Winter':
        final += hrizantemi * 3.75
        final += roses * 4.5
        final += tulips * 4.15
        if holiday == 'Y':
            final += final * 0.15
    return final


if season == 'Spring':
    price = calculate_price(season)

    if tulips > 7:
        price -= price * 0.05

    if hrizantemi + roses + tulips > 20:
        price -= price * 0.2

if season == 'Summer':
    price = calculate_price(season)

    if hrizantemi + roses + tulips > 20:
        price -= price * 0.2

if season == 'Autumn':
    price = calculate_price(season)

    if hrizantemi + roses + tulips > 20:
        price -= price * 0.2

if season == 'Winter':
    price = calculate_price(season)

    if roses >= 10:
        price -= price * 0.1

    if hrizantemi + roses + tulips > 20:
        price -= price * 0.2

price += 2
print(f'{price:.2f}')
