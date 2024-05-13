tshirt = float(input())
reward_sum = float(input())

shorts = tshirt * 0.75
socks = shorts * 0.20
shoes = (shorts + tshirt) * 2
check = shorts + socks + shoes + tshirt
check = check - check * 0.15

if check >= reward_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {check:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {reward_sum - check:.2f} lv. more.')
