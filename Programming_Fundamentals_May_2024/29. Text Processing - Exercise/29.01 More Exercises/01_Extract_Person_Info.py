n = int(input())
for i in range(n):
    name = ""
    age = ""
    is_name = False
    is_age = False
    line = input()
    for c in line:
        if is_name:
            name += c
        if is_age:
            age += c
        if c == "@":
            is_name = True
        elif c == "|":
            is_name = False
        elif c == "#":
            is_age = True
        elif c == "*":
            is_age = False
    print(f"{name[:-1]} is {age[:-1]} years old.")
