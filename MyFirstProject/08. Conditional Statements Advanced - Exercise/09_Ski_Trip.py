stay_days = int(input())
room_type = input()
grade = input()

price = 0

if room_type == 'room for one person':
    price = (stay_days - 1) * 18
elif room_type == 'apartment':
    if stay_days < 10:
        price = (stay_days - 1) * 25
        price -= price * 0.3
    elif 10 <= stay_days <= 15:
        price = (stay_days - 1) * 25
        price -= price * 0.35
    elif stay_days > 15:
        price = (stay_days - 1) * 25
        price -= price * 0.5

elif room_type == 'president apartment':
    if stay_days < 10:
        price = (stay_days - 1) * 35
        price -= price * 0.1
    elif 10 <= stay_days <= 15:
        price = (stay_days - 1) * 35
        price -= price * 0.15
    elif stay_days > 15:
        price = (stay_days - 1) * 35
        price -= price * 0.2

if grade == 'positive':
    price += price * 0.25
else:
    price -= price * 0.1

print(f'{price:.2f}')
