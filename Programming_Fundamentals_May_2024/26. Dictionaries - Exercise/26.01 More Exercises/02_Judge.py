contests = {}
while True:
    command = input()
    if command == "no more time":
        break
    line = command.split(" -> ")
    user = line[0]
    contest = line[1]
    points = int(line[2])
    if contest not in contests:
        contests[contest] = {user: points}
    else:
        if user not in contests[contest].values():
            contests[contest][user] = points
        else:
            current = contests[contest][user]
            contests[contest][user] = max(current, points)

user_rating = {}
for contest, users in contests.items():
    print(f"{contest}: {len(users)} participants")
    sorted_users = dict(reversed(sorted(users.items(), key=lambda x: x[1])))
    id = 1
    for user, points in sorted_users.items():
        if user not in user_rating:
            user_rating[user] = points
        else:
            user_rating[user] += points
    for key in sorted_users:
        points = sorted_users[key]
        print(f"{id}. {key} <::> {points}")
        id += 1

print("Individual standings:")
num = 1
sorted_user_rating = dict(reversed(sorted(user_rating.items(), key=lambda x: x[1])))
for user, points in sorted_user_rating.items():
    print(f"{num}. {user} -> {points}")
    num += 1
