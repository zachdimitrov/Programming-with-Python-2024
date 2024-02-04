years = int(input())
price = float(input())
toy = int(input())
all_sum = 0
money = 10

for i in range(1, years + 1):
    if i % 2 == 0:
        all_sum += money - 1
        money += 10
    else:
        all_sum += toy

if all_sum >= price:
    print(f'Yes! {all_sum - price:.2f}')
else:
    print(f'No! {price - all_sum:.2f}')
