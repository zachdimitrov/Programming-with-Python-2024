hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

difference = hour_exam * 60 + minute_exam - hour_arrival * 60 - minute_arrival

if hour_exam == hour_arrival and minute_exam == minute_arrival:
    print('On time')
elif difference < -59:
    difference = abs(difference)
    print('Late')
    dif_min = '' if difference % 60 > 9 else '0'
    print(f'{difference // 60}:{dif_min}{difference % 60} hours after the start.')
elif -59 <= difference < 0:
    difference = abs(difference)
    print('Late')
    print(f'{difference} minutes after the start')
elif 0 < difference <= 30:
    print('On time')
    print(f'{difference} minutes before the start')
elif 30 < difference <= 59:
    print('Early')
    print(f'{difference} minutes before the start')
elif difference >= 60:
    print('Early')
    dif_min = '' if difference % 60 > 9 else '0'
    print(f'{difference // 60}:{dif_min}{difference % 60} hours before the start.')
