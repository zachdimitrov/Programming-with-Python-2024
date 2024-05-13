area = int(input()) * int(input())
eaten = 0
left = area

while left > 0:
    command = input()
    if command == 'STOP':
        print(f'{left} pieces are left.')
        break
    else:
        to_eat = int(command)
        left -= to_eat

if left < 0:
    print(f'No more cake left! You need {abs(left)} pieces more.')
