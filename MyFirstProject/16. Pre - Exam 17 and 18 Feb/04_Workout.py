from math import ceil

days = int(input())
distance = float(input())
all_distance = distance

for i in range(0, days):
    percent = int(input())
    distance = distance + distance * percent / 100
    all_distance += distance

if all_distance >= 1000:
    print(f'You\'ve done a great job running {ceil(all_distance - 1000)} more kilometers!')
else:
    print(f'Sorry Mrs. Ivanova, you need to run {ceil(1000 - all_distance)} more kilometers')
