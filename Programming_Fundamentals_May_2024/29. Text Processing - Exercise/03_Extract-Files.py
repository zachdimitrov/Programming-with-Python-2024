path = input()
rev_file = ""
for i in range(len(path) - 1, 0, -1):
    if path[i] == "\\":
        break
    rev_file += path[i]

file = rev_file[::-1].split(".")
print(f"File name: {file[0]}")
print(f"File extension: {file[1]}")
