def check(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


destination = ''
needed = 1
collected = 0
income = 0
got_needed = False

while True:
    command = input()
    if command == 'End':
        break
    elif not check(command):
        destination = command
        got_needed = False
    elif check(command):
        if got_needed:
            income = income + float(command)
            collected += income
        else:
            got_needed = True
            needed = float(command)
    if income >= needed:
        print(f'Going to {destination}!')
        income = 0

    #print(f'Dest: {destination}')
    #print(f'Income: {income}')
    #print(f'Need: {needed}')
    #print('--------------')
