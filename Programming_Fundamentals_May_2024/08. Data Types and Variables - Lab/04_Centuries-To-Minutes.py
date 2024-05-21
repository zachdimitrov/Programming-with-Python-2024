import math

c = int(input())
year = 365.2422
years = math.floor(c * 100 * year)
print(f'{c} centuries = {c * 100} years = {years} days'
      f' = {years * 24} hours = {years * 24 * 60} minutes')
