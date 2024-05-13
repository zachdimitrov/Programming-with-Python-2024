hours = int(input())
minutes = int(input())
minutes_after = minutes + 15
hours_final = hours + minutes_after // 60
minutes_final = minutes_after % 60

if hours_final == 24:
    hours_final = 0

if minutes_final < 10:
    print(f'{hours_final}:0{minutes_final}')
else:
    print(f'{hours_final}:{minutes_final}')
