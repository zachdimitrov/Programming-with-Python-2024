n = int(input())
l = int(input())
symb_1 = 0
symb_2 = 0
symb_3 = ''
symb_4 = ''
symb_5 = 0

for i in range(1, n + 1):
    symb_1 = i
    for j in range(1, n + 1):
        symb_2 = j
        for a in range(97, 97 + l):
            symb_3 = chr(a)
            for b in range(97, 97 + l):
                symb_4 = chr(b)
                for k in range(2, n + 1):
                    if k > i and k > j:
                        symb_5 = k
                        print(str(i) + str(j) + symb_3 + symb_4 + str(symb_5) + ' ', end='')
                    else:
                        continue

