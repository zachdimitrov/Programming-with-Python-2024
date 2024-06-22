energy = 100
coins = 100
events = input().split("|")
completed = True

for e in events:
    command = e.split("-")
    event = command[0]
    num = int(command[1])

    if event == "rest":
        prev_energy = energy
        energy += num
        if energy >= 100:
            energy = 100
        energy_gain = energy - prev_energy
        print(f'You gained {energy_gain} energy.')
        print(f'Current energy: {energy}.')
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += num
            print(f"You earned {num} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= num:
            coins -= num
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            completed = False
            break

if completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
