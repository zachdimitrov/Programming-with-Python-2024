start = int(input())
end_int = int(input())
magic = int(input())
counter = 0
found = False

for i in range(start, end_int + 1):
    for j in range(start, end_int + 1):
        counter += 1
        if i + j == magic:
            found = True
            print(f'Combination N:{counter} ({i} + {j} = {magic})')
            break
    if found:
        break

if not found:
    print(f'{counter} combinations - neither equals {magic}')

