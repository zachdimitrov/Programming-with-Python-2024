start_gifts = input().split(" ")
command = input()

while command != "No Money":
    command_parts = command.split(" ")

    if command_parts[0] == "OutOfStock":
        to_remove = command_parts[1]
        for i in range(len(start_gifts)):
            if start_gifts[i] == to_remove:
                start_gifts[i] = "None"
    elif command_parts[0] == "Required":
        gift_to_add = command_parts[1]
        index_to_add = int(command_parts[2])
        if len(start_gifts) > index_to_add >= 0:
            start_gifts[index_to_add] = gift_to_add
    elif command_parts[0] == "JustInCase":
        last_item = command_parts[1]
        start_gifts[len(start_gifts) - 1] = last_item

    command = input()

for i in range(len(start_gifts) - 1, -1, -1):
    if "None" in start_gifts:
        start_gifts.remove("None")

print(*start_gifts, sep=" ")
