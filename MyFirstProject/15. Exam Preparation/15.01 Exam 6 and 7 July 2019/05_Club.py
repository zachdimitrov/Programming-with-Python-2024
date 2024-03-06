needed = float(input())
command = ''
earned = 0

while True:
    if earned >= needed:
        break
    command = input()
    if command == 'Party!':
        break
    number = int(input())
    price = len(command)
    check = number * price
    if check % 2 != 0:
        check = check - check * 0.25
    earned += check

if earned >= needed:
    print('Target acquired.')
else:
    print(f'We need {needed - earned:.2f} leva more.')
print(f'Club income - {earned:.2f} leva.')

