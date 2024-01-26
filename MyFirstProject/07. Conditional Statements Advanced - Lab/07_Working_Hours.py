hour = int(input())
day = input()

if (hour > 18 or hour < 10) or day == "Sunday":
    print('closed')
else:
    print('open')
