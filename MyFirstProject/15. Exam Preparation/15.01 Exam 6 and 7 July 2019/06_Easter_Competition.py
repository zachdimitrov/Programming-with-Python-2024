number = int(input())
max_score = -1
best_chef = ''

for i in range(0, number):
    chef = input()
    scores = 0
    while True:
        command = input()
        if command == 'Stop':
            break
        scores += int(command)
    print(f'{chef} has {scores} points.')
    if scores > max_score:
        max_score = scores
        best_chef = chef
        print(f'{chef} is the new number 1!')

print(f'{best_chef} won competition with {max_score} points!')
