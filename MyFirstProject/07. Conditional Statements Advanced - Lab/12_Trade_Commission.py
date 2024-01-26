city = input()
sales = float(input())
commission = 0
err = ''

if city == 'Sofia':
    if 0 < sales <= 500:
        commission = 5
    elif 500 < sales <= 1000:
        commission = 7
    elif 1000 < sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
    else:
        err = 'error'
elif city == 'Varna':
    if 0 < sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
    else:
        err = 'error'
elif city == 'Plovdiv':
    if 0 < sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8
    elif 1000 < sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5
    else:
        err = 'error'
else:
    err = 'error'

if err == '':
    print(f'{commission * sales * 0.01:.2f}')
else:
    print('error')
