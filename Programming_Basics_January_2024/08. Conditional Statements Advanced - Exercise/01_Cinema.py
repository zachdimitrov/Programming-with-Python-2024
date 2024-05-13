movie_type = input()
rows = int(input())
cols = int(input())

income = 0
capacity = rows * cols

if movie_type == 'Premiere':
    income = capacity * 12.00
elif movie_type == 'Normal':
    income = capacity * 7.50
elif movie_type == 'Discount':
    income = capacity * 5.00

print(f'{income:.2f} leva')
