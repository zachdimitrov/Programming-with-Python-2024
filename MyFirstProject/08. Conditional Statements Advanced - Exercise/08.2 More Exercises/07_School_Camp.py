season = input()  # Winter, Spring, Summer
group_type = input()  # boys, girls, mixed
students_count = int(input())
nights = int(input())

price = 0
sport = ''

if group_type == 'girls':
    if season == 'Winter':
        price = students_count * 9.6
        sport = 'Gymnastics'
    elif season == 'Spring':
        price = students_count * 7.2
        sport = 'Athletics'
    elif season == 'Summer':
        price = students_count * 15
        sport = 'Volleyball'
elif group_type == 'boys':
    if season == 'Winter':
        price = students_count * 9.6
        sport = 'Judo'
    elif season == 'Spring':
        price = students_count * 7.2
        sport = 'Tennis'
    elif season == 'Summer':
        price = students_count * 15
        sport = 'Football'
elif group_type == 'mixed':
    if season == 'Winter':
        price = students_count * 10
        sport = 'Ski'
    elif season == 'Spring':
        price = students_count * 9.5
        sport = 'Cycling'
    elif season == 'Summer':
        price = students_count * 20
        sport = 'Swimming'

price *= nights

if 10 <= students_count < 20:
    price -= price * 0.05
elif 20 <= students_count < 50:
    price -= price * 0.15
elif students_count >= 50:
    price -= price * 0.5

print(f'{sport} {price:.2f} lv.')
