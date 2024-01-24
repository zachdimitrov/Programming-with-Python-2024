age = float(input())
gender = input()

if gender == 'm':
    print(f'{"Master" if age < 16 else "Mr."}')
else:
    print(f'{"Miss" if age < 16 else "Ms."}')
    