a = int(input())
b = int(input())
max_comb = int(input())
comb = 0

is_finished = False

symb_A = ''
symb_B = ''
symb_x = 0
symb_y = 0
i = 35
j = 64

for k in range(1, a + 1):
    if comb >= max_comb:
        break
    symb_x = k
    for p in range(1, b + 1):
        if comb >= max_comb:
            break
        symb_A = chr(i)
        symb_B = chr(j)
        i += 1
        j += 1
        if i >= 56:
            i = 35
        if j >= 97:
            j = 64
        symb_y = p
        print(symb_A + symb_B + str(symb_x) + str(symb_y) + symb_B + symb_A, end='|')
        comb += 1

