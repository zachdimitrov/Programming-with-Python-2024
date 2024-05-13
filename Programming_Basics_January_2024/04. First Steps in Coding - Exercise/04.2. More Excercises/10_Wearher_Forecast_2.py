temp = float(input())
if 35 >= temp >= 26:
    print('Hot')
elif 25.9 >= temp >= 20.1:
    print('Warm')
elif 20 >= temp >= 15:
    print('Mild')
elif 14.9 >= temp >= 12:
    print('Cool')
elif 11.9 >= temp >= 5:
    print('Cold')
else:
    print('unknown')
