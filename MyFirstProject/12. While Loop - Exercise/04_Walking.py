day_steps = 0

while True:
    message = input()
    if message == 'Going home':
        steps_last = int(input())
        if day_steps + steps_last >= 10000:
            print('Goal reached! Good job!')
            print(f'{steps_last + day_steps - 10000} steps over the goal!')
        else:
            print(f'{10000 - (day_steps + steps_last)} more steps to reach goal.')
        break

    steps_out = int(message)
    day_steps += steps_out
    if day_steps >= 10000:
        print('Goal reached! Good job!')
        print(f'{day_steps - 10000} steps over the goal!')
        break
