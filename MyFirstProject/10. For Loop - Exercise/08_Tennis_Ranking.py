import math

tournament_number = int(input())
init_points = int(input())
wins = 0
points = init_points

for i in range(0, tournament_number):
    place = input()
    if place == 'W':
        points += 2000
        wins += 1
    elif place == 'F':
        points += 1200
    elif place == 'SF':
        points += 720

print(f'Final points: {points}')
print(f'Average points: {math.floor((points - init_points)/tournament_number)}')
print(f'{wins / tournament_number * 100:.2f}%')
