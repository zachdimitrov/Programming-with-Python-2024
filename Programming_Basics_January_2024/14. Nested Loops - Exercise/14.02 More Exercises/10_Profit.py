one_all = int(input())
two_all = int(input())
five_all = int(input())
all_sum = int(input())

for i in range(0, one_all + 1):
    for j in range(0, two_all + 1):
        for k in range(0, five_all + 1):
            if i * 1 + j * 2 + k * 5 == all_sum:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {all_sum} lv.')
