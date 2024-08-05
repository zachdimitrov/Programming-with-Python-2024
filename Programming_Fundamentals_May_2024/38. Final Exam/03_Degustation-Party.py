guests = {}
unliked = 0

while True:
    command = input()
    if command == "Stop":
        break

    line = command.split("-")
    name = line[1]
    meal = line[2]
    if line[0] == "Like":
        if name in guests:
            if meal not in guests[name]:
                guests[name].append(meal)
        else:
            guests[name] = [meal]
    elif line[0] == "Dislike":
        if name in guests:
            if meal not in guests[name]:
                print(f"{name} doesn't have the {meal} in his/her collection.")
            else:
                unliked += 1
                print(f"{name} doesn't like the {meal}.")
                guests[name].remove(meal)
        else:
            print(f"{name} is not at the party.")

for g, meals in guests.items():
    print(f"{g}: {', '.join(meals)}")
print(f"Unliked meals: {unliked}")
