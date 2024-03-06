dancers = int(input())
points = float(input())
season = input() # summer winter
place = input() # Bulgaria Abroad

reward = 0

if place == 'Bulgaria':
    reward = dancers * points
    if season == 'summer':
        reward = reward - reward * 0.05
    elif season == 'winter':
        reward = reward - reward * 0.08
elif place == 'Abroad':
    reward = dancers * points
    reward = reward * 1.5
    if season == 'summer':
        reward = reward - reward * 0.1
    elif season == 'winter':
        reward = reward - reward * 0.15

charity = reward * 0.75
reward = reward - charity

print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {reward / dancers:.2f}')
