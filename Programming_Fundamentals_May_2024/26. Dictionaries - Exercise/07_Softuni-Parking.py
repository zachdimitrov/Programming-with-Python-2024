n = int(input())
users = {}
for i in range(n):
    line = input().split(" ")
    command = line[0]
    name = line[1]
    if len(line) > 2:
        plate = line[2]

    if command == "register":
        if name not in users:
            users[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[name]}")
    elif command == "unregister":
        if name not in users:
            print(f"ERROR: user {name} not found")
        else:
            users.pop(name)
            print(f"{name} unregistered successfully")

for name, plate in users.items():
    print(f"{name} => {plate}")
