cards = input().split(" ")
team_a = list(range(1, 12))
team_b = list(range(1, 12))
terminated = False

for card in cards:
    card_list = card.split("-")
    team = card_list[0]
    player = int(card_list[1])
    if team == "A":
        if player in team_a:
            team_a.remove(player)
        if len(team_a) < 7:
            terminated = True
            break
    if team == 'B':
        if player in team_b:
            team_b.remove(player)
        if len(team_b) < 7:
            terminated = True
            break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminated:
    print('Game was terminated')
