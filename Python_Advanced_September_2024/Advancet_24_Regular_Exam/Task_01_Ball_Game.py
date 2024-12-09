from collections import deque

strengths = [int(x) for x in input().split()]
accuracies = deque([int(x) for x in input().split()])

goals = 0

while strengths and accuracies:
    next_strength = strengths.pop()
    next_acc = accuracies.popleft()
    goal_sum = next_acc + next_strength

    if goal_sum == 100:
        goals += 1
    elif goal_sum < 100:
        if next_strength < next_acc:
            accuracies.appendleft(next_acc)
        elif next_strength > next_acc:
            strengths.append(next_strength)
        elif next_strength == next_acc:
            strengths.append(goal_sum)
    elif goal_sum > 100:
        next_strength -= 10
        strengths.append(next_strength)
        accuracies.append(next_acc)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")
elif goals > 3:
    print("Paul performed remarkably well!")

if goals:
    print(f"Goals scored: {goals}")

if strengths:
    print(f"Strength values left: {', '.join([str(x) for x in strengths])}")
if accuracies:
    print(f"Accuracy values left: {', '.join([str(x) for x in accuracies])}")

