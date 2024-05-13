month = input()
nights = int(input())

studio_price = 0
apt_price = 0
studio_discount = 0
apt_discount = 0

if nights > 14:
    apt_discount = 0.1

if month == 'May' or month == 'October':
    if 7 < nights <= 14:
        studio_discount = 0.05
    elif nights > 14:
        studio_discount = 0.3

    studio_price = nights * 50 - nights * 50 * studio_discount
    apt_price = nights * 65 - nights * 65 * apt_discount

elif month == 'June' or month == 'September':
    if nights > 14:
        studio_discount = 0.2

    studio_price = nights * 75.2 - nights * 75.2 * studio_discount
    apt_price = nights * 68.7 - nights * 68.7 * apt_discount

elif month == 'July' or month == 'August':
    studio_price = nights * 76
    apt_price = nights * 77 - nights * 77 * apt_discount

print(f'Apartment: {apt_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
