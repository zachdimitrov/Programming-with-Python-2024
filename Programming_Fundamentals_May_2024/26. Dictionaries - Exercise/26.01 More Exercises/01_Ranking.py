contests = {}
users = {}

while True:
    command = input()
    if command == "end of contests":
        break
    line = command.split(":")
    name = line[0]
    pasw = line[1]
    if name not in contests:
        contests[name] = pasw

while True:
    command = input()
    if command == "end of submissions":
        break
    line = command.split("=>")
    contest = line[0]
    pasw = line[1]
    user = line[2]
    points = int(line[3])
    if contest in contests and pasw == contests[contest]:
        if user not in users:
            users[user] = {}
            users[user][contest] = points
        else:
            if contest not in users[user]:
                users[user][contest] = points
            else:
                current = users[user][contest]
                users[user][contest] = max(points, current)

max_points = 0
best_user = ""
for user, contests in users.items():
    all_points = 0
    for val in contests.values():
        all_points += val

    if all_points > max_points:
        max_points = all_points
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")
print("Ranking:")
sorted_users = dict(sorted(users.items()))
for user, contests in sorted_users.items():
    print(f"{user}")
    sorted_contests = dict(reversed(sorted(contests.items(), key=lambda x: x[1])))
    for contest, points in sorted_contests.items():
        print(f"#  {contest} -> {points}")
