from math import floor

record = float(input())
distance = float(input())
meter_speed = float(input())

time = distance * meter_speed + floor(distance / 15) * 12.5

if time < record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {time - record:.2f} seconds slower.')

