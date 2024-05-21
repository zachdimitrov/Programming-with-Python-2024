count = int(input())
highest_value = 0
highest_data = (0, 0, 0)
for i in range(0, count):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if highest_value < value:
        highest_value = value
        highest_data = (weight, time_needed, quality)

print(f'{highest_data[0]} : {highest_data[1]} = {int(highest_value)} ({highest_data[2]})')
