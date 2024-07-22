usernames = input().split(", ")
for name in usernames:
    is_valid = True
    if len(name) < 3 or len(name) > 16:
        is_valid = False
    for c in name:
        if not (c.isalpha() or c.isdigit() or c == "_" or c == "-"):
            is_valid = False
    if is_valid:
        print(name)

