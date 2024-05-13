n1 = int(input())
n2 = int(input())
operator = input()
even_odd = ''
dev_by_zero = False

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    if n2 == 0:
        dev_by_zero = True
    else:
        result = n1 / n2
elif operator == '%':
    if n2 == 0:
        dev_by_zero = True
    else:
        result = n1 % n2
else:
    dev_by_zero = True

if dev_by_zero:
    print(f'Cannot divide {n1} by zero')
else:
    even_odd = 'even' if result % 2 == 0 else 'odd'
    if operator == '+' or operator == '-' or operator == '*':
        print(f'{n1} {operator} {n2} = {result} - {even_odd}')
    elif operator == '/':
        print(f'{n1} / {n2} = {result:.2f}')
    elif operator == '%':
        print(f'{n1} % {n2} = {result}')
