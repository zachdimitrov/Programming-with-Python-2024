def return_coins(coins, remain):
    coins.sort(reverse=True)
    returned_count = {}

    idx = 0
    while idx < len(coins) and remain != 0:
        returned = remain // coins[idx]
        remain %= coins[idx]
        if returned > 0:
            returned_count[coins[idx]] = returned

        idx += 1
    if remain != 0:
        return "Error"
    result = f"Number of coins to take: {sum(returned_count.values())}\n"
    for coin, number in returned_count.items():
        result += f"{number} coin(s) with value {coin}\n"
    return result


coin_values = [int(x) for x in input().split(", ")]
money = int(input())

print(return_coins(coin_values, money))

##not recursive solution
# num_coins = 0
# list_coins = {}
# error = False
#
# while coin_values:
#     coin = coin_values.pop()
#     if money >= coin:
#         coins = money // coin
#         money = money - coin * coins
#         num_coins += coins
#         list_coins[coin] = coins
#     if money == 0:
#         break
#     if not coin_values and money > 0:
#         error = True
#         break
#
# if not error:
#     print(f"Number of coins to take: {num_coins}")
#     for coin, number in list_coins.items():
#         print(f"{number} coin(s) with value {coin}")
# else:
#     print("Error")

