miner = {}
while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command not in miner:
        miner[command] = quantity
    else:
        miner[command] += quantity

for key, value in miner.items():
    print(f"{key} -> {value}")
    