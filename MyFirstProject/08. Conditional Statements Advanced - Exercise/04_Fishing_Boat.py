budget = int(input())
season = input()
fishermen = int(input())
check = 0


def calc_check(pr, number):
    final = 0
    if number <= 6:
        final = pr - pr * 0.1
    elif 7 <= number <= 11:
        final = pr - pr * 0.15
    elif number >= 12:
        final = pr - pr * 0.25
    return final


if season == 'Spring':
    check = calc_check(3000, fishermen)
    if fishermen % 2 == 0:
        check -= check * 0.05
elif season == 'Summer':
    check = calc_check(4200, fishermen)
    if fishermen % 2 == 0:
        check -= check * 0.05
elif season == 'Autumn':
    check = calc_check(4200, fishermen)
elif season == 'Winter':
    check = calc_check(2600, fishermen)
    if fishermen % 2 == 0:
        check -= check * 0.05

if budget >= check:
    print(f'Yes! You have {budget - check:.2f} leva left.')
else:
    print(f'Not enough money! You need {check - budget:.2f} leva.')
