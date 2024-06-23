experience_needed = float(input())
battle_count = int(input())
gained = 0

for i in range(1, battle_count + 1):
    current_earned = float(input())
    if i % 3 == 0:
        gained = gained + current_earned * 1.15
    elif i % 5 == 0:
        gained = gained + current_earned * 0.9
    elif i % 15 == 0:
        gained = gained + current_earned * 1.05
    else:
        gained += current_earned
    if gained >= experience_needed:
        print(f'Player successfully collected his needed experience for {i} battles.')
        break

if gained < experience_needed:
    print(f'Player was not able to collect the needed experience, {experience_needed - gained:.2f} more needed.')
