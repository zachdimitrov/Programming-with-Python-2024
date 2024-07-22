players = {}
total = {}
while True:
    command = input()
    if command == "Season end":
        break
    if "->" in command:
        line = command.split(" -> ")
        user = line[0]
        skill = line[1]
        points = int(line[2])
        if user not in players:
            players[user] = {skill: points}
            total[user] = points
        else:
            if skill not in players[user]:
                players[user][skill] = points
                total[user] += points
            else:
                if players[user][skill] < points:
                    total[user] -= players[user][skill]
                    players[user][skill] = points
                    total[user] += points

    if "vs" in command:
        line = command.split(" vs ")
        user1 = line[0]
        user2 = line[1]
        if user1 in players and user2 in players:
            for skill in players[user1]:
                if skill in players[user2]:
                    if total[user1] == total[user2]: #players[user1][skill] == players[user2][skill]:
                        continue
                    else:
                        if total[user1] > total[user2]:
                            del players[user2]
                            del total[user2]
                        elif total[user1] < total[user2]:
                            del players[user1]
                            del total[user1]

sorted_players = dict(sorted(players.items()))
sorted_totals = dict(sorted(total.items(), key=lambda x: x[1], reverse=True))

for user in sorted_totals:
    print(f"{user}: {total[user]} skill")

    skills = players[user]
    sorted_skills = dict(sorted(skills.items(), key=lambda x: x[1], reverse=True))
    for skill, points in sorted_skills.items():
        print(f"- {skill} <::> {points}")
