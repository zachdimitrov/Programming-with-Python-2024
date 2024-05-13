actor = input()
points = float(input())
n = int(input())

for i in range(0, n):
    judge_name = input()
    judge_points = float(input())
    points += len(judge_name) * judge_points * 0.5
    if points > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {points:.1f}!')
        break

if points <= 1250.5:
    print(f'Sorry, {actor} you need {1250.5 - points:.1f} more!')
