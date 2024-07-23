import re
pattern = r"\d+"

line = input()
while line:
    match = re.findall(pattern, line)
    for m in match:
        print(f"{m}", end=" ")
    line = input()