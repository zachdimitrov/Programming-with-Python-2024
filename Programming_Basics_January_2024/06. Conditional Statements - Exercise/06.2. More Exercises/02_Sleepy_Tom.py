rest_days = int(input())

work_days = 365 - rest_days

play_hours = rest_days * 127 + work_days * 63

if play_hours <= 30000:
    remaining_minutes = 30000 - play_hours
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    more_minutes = play_hours - 30000
    hours = more_minutes // 60
    minutes = more_minutes % 60
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
