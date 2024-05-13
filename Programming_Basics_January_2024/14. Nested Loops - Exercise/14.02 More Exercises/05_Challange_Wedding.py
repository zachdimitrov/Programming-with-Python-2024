men = int(input())
women = int(input())
max_tables = int(input())
tables = max_tables

for i in range(1, men + 1):
    for j in range(1, women + 1):
        if tables <= 0:
            break
        print(f'({i} <-> {j})' + ' ', end='')
        tables = tables - 1
