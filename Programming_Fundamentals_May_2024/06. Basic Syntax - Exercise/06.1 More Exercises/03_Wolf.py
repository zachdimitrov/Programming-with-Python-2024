sheeps = input().split(', ')

if sheeps[len(sheeps)-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    sheeps.reverse()
    i = 0
    for sheep in sheeps:
        if sheep == 'wolf':
            print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
            break
        i += 1
