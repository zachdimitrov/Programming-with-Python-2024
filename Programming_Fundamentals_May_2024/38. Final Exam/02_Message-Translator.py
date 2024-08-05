import re

n = int(input())

for i in range(n):
    message = input()
    pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]+)\]"
    groups = re.findall(pattern, message)
    #print(groups)
    if not groups:
        print("The message is invalid")
    else:
        command = groups[0][0]
        message = groups[0][1]
        collected = []
        for c in message:
            collected.append(str(ord(c)))
        print(f"{command}: {' '.join(collected)}")
