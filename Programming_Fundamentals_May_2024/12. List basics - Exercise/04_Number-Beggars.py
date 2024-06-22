sums = input().split(', ')
number_beggars = int(input())
beggars = [0] * number_beggars

while len(sums) > 0:
    for i in range(len(beggars)):
        if len(sums) > 0:
            beggars[i] += int(sums[0])
            sums.remove(sums[0])
        else:
            break

print(beggars)
