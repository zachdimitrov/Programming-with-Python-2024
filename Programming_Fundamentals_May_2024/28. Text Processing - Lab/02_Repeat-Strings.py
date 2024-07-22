strings = input().split(" ")
for s in strings:
    print(f"{s*len(s)}", end="")
