from math import ceil
name = input()
episode_time = int(input())
rest_time = int(input())

lunch_time = rest_time * 0.125
relax_time = rest_time * 0.25
left_time = rest_time - lunch_time - relax_time

if left_time >= episode_time:
    print(f'You have enough time to watch {name} and left with {ceil(left_time - episode_time)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name}, you need {ceil(episode_time - left_time)} more minutes.')
