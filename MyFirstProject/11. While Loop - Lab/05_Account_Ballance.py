total = 0
while True:
    command = input()
    if command == 'NoMoreMoney':
        print(f'Total: {total:.2f}')
        break
    money = float(command)
    if money < 0:
        print('Invalid operation!')
        print(f'Total: {total:.2f}')
        break
    total += money
    print(f'Increase: {money:.2f}')
