string = input()
for d in string:
    if d.isdigit():
        print(f"{d}", end="")
print("")

for l in string:
    if l.isalpha():
        print(f"{l}", end="")
print("")

for c in string:
    if (not c.isdigit()) and (not c.isalpha()):
        print(f"{c}", end="")
print("")
