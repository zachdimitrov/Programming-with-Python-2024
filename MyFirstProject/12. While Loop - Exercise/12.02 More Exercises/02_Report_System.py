required = int(input())
collected = 0
rnd = 0
cash_rnd = 0
card_rnd = 0
cash_payed = 0
card_payed = 0

while True:
    command = input()
    if command == 'End':
        print('Failed to collect required money for charity.')
        break
    else:
        rnd += 1
        price = int(command)
        if rnd % 2 == 0:
            if price < 10:
                print('Error in transaction!')
            else:
                collected += price
                card_payed += price
                card_rnd += 1
                print('Product sold!')
        else:
            if price > 100:
                print('Error in transaction!')
            else:
                collected += price
                cash_payed += price
                cash_rnd += 1
                print('Product sold!')
        if collected >= required:
            avg_cash = cash_payed / cash_rnd
            avg_card = card_payed / card_rnd
            print(f'Average CS: {avg_cash:.2f}')
            print(f'Average CC: {avg_card:.2f}')
            break
