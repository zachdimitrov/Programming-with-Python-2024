n = int(input())
opened = False
closed = True
ended = False
for i in range(0, n):
    char = input()
    if char == '(':
        if closed:
            opened = True
            closed = False
        else:
            print('UNBALANCED')
            ended = True
            break
    elif char == ')':
        if opened:
            closed = True
            opened = False
        else:
            print('UNBALANCED')
            ended = True
            break

if closed and not ended:
    print('BALANCED')
elif not ended and not closed:
    print('UNBALANCED')
