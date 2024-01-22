ex_price = float(input())
n_puzzles = int(input())
n_dolls = int(input())
n_bears = int(input())
n_minions = int(input())
n_trucks = int(input())

n_total = n_puzzles + n_dolls + n_bears + n_trucks + n_minions
sum_total = n_puzzles * 2.6\
            + n_dolls * 3\
            + n_bears * 4.1\
            + n_minions * 8.2\
            + n_trucks * 2

if n_total >= 50:
    sum_total -= sum_total * 0.25

sum_total -= sum_total * 0.1

if sum_total >= ex_price:
    print(f'Yes! {sum_total - ex_price:.2f} lv left.')
else:
    print(f'Not enough money! {ex_price - sum_total:.2f} lv needed.')

    