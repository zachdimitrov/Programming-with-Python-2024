from math import floor
pages = int(input())
pages_per_hour = int(input())
days = int(input())
print(floor((pages / pages_per_hour)/days))

