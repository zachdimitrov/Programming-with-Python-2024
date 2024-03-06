start = int(input())
finish = int(input())

for i in range(start, finish + 1):
    even_sum = 0
    odd_sum = 0
    position = 0
    for ch in str(i):
        position += 1
        if position % 2 == 0:
            even_sum += int(ch)
        else:
            odd_sum += int(ch)
    if odd_sum == even_sum:
        print(i, end=' ')
    else:
        continue
