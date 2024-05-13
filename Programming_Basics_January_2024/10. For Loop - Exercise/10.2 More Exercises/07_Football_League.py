capacity = int(input())
all_fans = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for i in range(0, all_fans):
    sector = input()
    if sector == 'A':
        a_sector += 1
    elif sector == 'B':
        b_sector += 1
    elif sector == 'V':
        v_sector += 1
    elif sector == 'G':
        g_sector += 1

print(f'{a_sector / all_fans * 100:.2f}%')
print(f'{b_sector / all_fans * 100:.2f}%')
print(f'{v_sector / all_fans * 100:.2f}%')
print(f'{g_sector / all_fans * 100:.2f}%')
print(f'{all_fans / capacity * 100:.2f}%')
