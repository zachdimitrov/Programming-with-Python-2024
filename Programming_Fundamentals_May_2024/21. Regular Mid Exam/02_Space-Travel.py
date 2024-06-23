route = input().split("||")
fuel = int(input())
ammo = int(input())

for route_part_string in route:
    route_part = route_part_string.split()
    command = route_part[0]
    if command == 'Titan':
        print('You have reached Titan, all passengers are safe.')
        break
    elif command == 'Travel':
        light_years = int(route_part[1])
        if fuel >= light_years:
            fuel -= light_years
            print(f'The spaceship travelled {light_years} light-years.')
        else:
            print('Mission failed.')
            break
    elif command == 'Enemy':
        armor = int(route_part[1])
        if ammo >= armor:
            ammo -= armor
            print(f'An enemy with {armor} armour is defeated.')
        else:
            if fuel >= armor * 2:
                fuel = fuel - armor * 2
                print(f'An enemy with {armor} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break
    elif command == 'Repair':
        amount = int(route_part[1])
        fuel += amount
        ammo += amount * 2
        print(f'Ammunitions added: {amount * 2}.')
        print(f'Fuel added: {amount}.')
