detergent = int(input())
volume = detergent * 750
loads = 0
dishes = 0
pots = 0

while volume > 0:
    command = input()
    if command == 'End':
        print('Detergent was enough!')
        print(f'{dishes} dishes and {pots} pots were washed.')
        print(f'Leftover detergent {volume} ml.')
        break
    else:
        number = int(command)
        loads += 1
        if loads % 3 == 0:
            volume -= number * 15
            pots += number
        else:
            volume -= number * 5
            dishes += number

if volume < 0:
    print(f'Not enough detergent, {abs(volume)} ml. more necessary!')
