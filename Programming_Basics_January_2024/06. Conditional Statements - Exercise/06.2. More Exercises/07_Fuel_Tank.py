fuel = input()
liters = float(input())

if fuel == 'Diesel' or fuel =='Gas' or fuel == 'Gasoline':
    if liters < 25:
        print(f'Fill your tank with {fuel.lower()}!')
    else:
        print(f'You have enough {fuel.lower()}.')
else:
    print('Invalid fuel!')
