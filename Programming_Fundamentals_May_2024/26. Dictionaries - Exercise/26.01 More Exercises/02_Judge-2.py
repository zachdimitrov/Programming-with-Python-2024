contests = {}
users = {}

while True:
    input_line = input().split(" -> ")
    if input_line[0] == "no more time":
        break

    username = input_line[0]
    contest = input_line[1]
    points = int(input_line[2])

    if contest not in contests:
        contests[contest] = {username: points}
    else:
        if username not in contests[contest]:
            contests[contest][username] = points
        else:
            if contests[contest][username] < points:
                contests[contest][username] = points

for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    for i, (name, points) in enumerate(sorted_participants, start=1):
        print(f"{i}. {name} <::> {points}")

print("Individual standings:")

for contest in contests.values():
    for name, points in contest.items():
        if name not in users:
            users[name] = points
        else:
            users[name] += points

sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
for i, (name, total_points) in enumerate(sorted_users, start=1):
    print(f"{i}. {name} -> {total_points}")
