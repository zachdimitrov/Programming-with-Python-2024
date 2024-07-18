results = {}
submissions = {}
while True:
    command = input()
    if command == "exam finished":
        break
    line = command.split("-")
    user = line[0]
    language = line[1]
    points = 0
    if len(line) > 2:
        points = int(line[2])
    if language != "banned":
        if user not in results:
            results[user] = points
        else:
            current = results[user]
            results[user] = max(current, points)
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        if user in results:
            results.pop(user, None)

print("Results:")
for key, elem in results.items():
    print(f"{key} | {elem}")
print("Submissions:")
for sub, num in submissions.items():
    print(f"{sub} - {num}")
