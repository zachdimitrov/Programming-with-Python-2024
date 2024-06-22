times = list(map(int, input().split(" ")))
left_racer = 0
right_racer = 0

for i in range(0, len(times)//2):
    if times[i] != 0:
        left_racer += times[i]
    else:
        left_racer = left_racer * 0.8

for j in range(len(times) - 1, len(times)//2, -1):
    if times[j] != 0:
        right_racer += times[j]
    else:
        right_racer = right_racer * 0.8

if left_racer < right_racer:
    print(f'The winner is left with total time: {left_racer:.1f}')
else:
    print(f'The winner is right with total time: {right_racer:.1f}')
