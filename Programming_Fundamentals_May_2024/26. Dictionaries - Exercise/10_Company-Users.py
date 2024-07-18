company = {}
while True:
    command = input()
    if command == "End":
        break
    line = command.split(" -> ")
    name = line[0]
    id = line[1]
    if name not in company:
        company[name] = [id]
    else:
        if id not in company[name]:
            company[name].append(id)

for name, ids in company.items():
    print(name)
    for id in ids:
        print(f"-- {id}")
