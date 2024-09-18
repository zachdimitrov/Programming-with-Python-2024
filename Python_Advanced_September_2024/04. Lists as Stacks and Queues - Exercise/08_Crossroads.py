from collections import deque

green_duration = int(input())
free_window = int(input())
command = input()
cars = deque()
passed = 0
crashed = False

while command != "END":
    if command != "green":
        cars.append(command)
    else:
        seconds_left = green_duration + free_window
        while len(cars) > 0:
            if seconds_left > free_window:
                next_car = cars.popleft()
                if seconds_left >= len(next_car):
                    seconds_left = seconds_left - len(next_car)
                    passed += 1
                else:
                    crash_symbol = next_car[seconds_left:seconds_left + 1]
                    print("A crash happened!")
                    print(f"{next_car} was hit at {crash_symbol}.")
                    crashed = True
            else:
                break
            if crashed:
                break
    if crashed:
        break
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")
