visitors = int(input())

back = 0
chest = 0
legs = 0
abbs = 0
pro_shake = 0
pro_bar = 0

number_workout = 0
number_eat = 0

for i in range(0, visitors):
    command = input()
    if command == 'Back':
        back += 1
        number_workout += 1
    elif command == 'Chest':
        chest += 1
        number_workout += 1
    elif command == 'Legs':
        legs += 1
        number_workout += 1
    elif command == 'Abs':
        abbs += 1
        number_workout += 1
    elif command == 'Protein shake':
        pro_shake += 1
        number_eat += 1
    elif command == 'Protein bar':
        pro_bar += 1
        number_eat += 1

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abbs} - abs')
print(f'{pro_shake} - protein shake')
print(f'{pro_bar} - protein bar')
print(f'{number_workout / visitors * 100:.2f}% - work out')
print(f'{number_eat / visitors * 100:.2f}% - protein')
