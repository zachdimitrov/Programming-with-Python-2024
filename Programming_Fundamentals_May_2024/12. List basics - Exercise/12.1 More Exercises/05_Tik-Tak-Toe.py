top_line = list(map(int, input().split(" ")))
mid_line = list(map(int, input().split(" ")))
bot_line = list(map(int, input().split(" ")))

winner = ""

if top_line[0] == top_line[1] and top_line[1] == top_line[2]:
    if top_line[0] == 1:
        winner = "First"
    elif top_line[0] == 2:
        winner = "Second"
elif mid_line[0] == mid_line[1] and mid_line[1] == mid_line[2]:
    if mid_line[0] == 1:
        winner = "First"
    elif mid_line[0] == 2:
        winner = "Second"
elif bot_line[0] == bot_line[1] and bot_line[1] == bot_line[2]:
    if bot_line[0] == 1:
        winner = "First"
    elif bot_line[0] == 2:
        winner = "Second"
elif top_line[0] == mid_line[0] and mid_line[0] == bot_line[0]:
    if top_line[0] == 1:
        winner = "First"
    elif top_line[0] == 2:
        winner = "Second"
elif top_line[1] == mid_line[1] and mid_line[1] == bot_line[1]:
    if top_line[1] == 1:
        winner = "First"
    elif top_line[1] == 2:
        winner = "Second"
elif top_line[2] == mid_line[2] and mid_line[2] == bot_line[2]:
    if top_line[2] == 1:
        winner = "First"
    elif top_line[2] == 2:
        winner = "Second"
elif top_line[0] == mid_line[1] and mid_line[1] == bot_line[2]:
    if top_line[0] == 1:
        winner = "First"
    elif top_line[0] == 2:
        winner = "Second"
elif top_line[2] == mid_line[1] and mid_line[1] == bot_line[0]:
    if top_line[2] == 1:
        winner = "First"
    elif top_line[2] == 2:
        winner = "Second"

if winner == "":
    print("Draw!")
else:
    print(f"{winner} player won")
