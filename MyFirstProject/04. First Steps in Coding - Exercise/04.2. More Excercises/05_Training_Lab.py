from math import floor
w = float(input('Length of hall: '))
h = float(input('Width of hall: '))
number_by_width = floor((h - 1) / 0.7)
# print(number_by_width)
number_by_length = floor(w / 1.2)
# print(number_by_length)
print(number_by_width * number_by_length - 3)
