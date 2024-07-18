force = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        line = command.split(" | ")
        side = line[0]
        user = line[1]
        exists = False
        for key, value in force.items():
            if user in value:
                exists = True
        if exists:
            continue
        if side not in force:
            force[side] = [user]
        else:
            force[side].append(user)
    elif "->" in command:
        line = command.split(" -> ")
        user = line[0]
        side = line[1]
        for key, value in force.items():
            if user in value:
                force[key].remove(user)
        if side not in force:
            force[side] = [user]
        else:
            force[side].append(user)
        print(f"{user} joins the {side} side!")

for side, users in force.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
