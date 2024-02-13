volume = int(input()) * int(input()) * int(input())
left = volume

while left > 0:
    command = input()
    if command == 'Done':
        print(f'{left} Cubic meters left.')
        break
    else:
        left -= int(command)

if left < 0:
    print(f'No more free space! You need {abs(left)} Cubic meters more.')
