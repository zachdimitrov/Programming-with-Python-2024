import re
lines_num = int(input())
attacked = []
destroyed = []
for i in range(lines_num):
    line = input()
    pattern = r"(t|T)|(S|s)|(a|A)|(r|R)"
    letters = re.findall(pattern, line)
    count = 0
    for group in letters:
        for letter in group:
            if letter:
                count += 1
    new_line = ""
    for char in line:
        new_char = chr(ord(char) - count)
        new_line += new_char
    reg = r"@([A-Za-z]+).*:(\d+).*!(A|D)!.*->(\d+)"
    result = re.findall(reg, new_line)
    if result:
        if result[0][2] == "A":
            attacked.append(result[0][0])
        elif result[0][2] == "D":
            destroyed.append(result[0][0])
print(f"Attacked planets: {len(attacked)}")
if attacked:
    sort_attacked = sorted(attacked)
    for planet in sort_attacked:
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed)}")
if destroyed:
    sort_destroyed = sorted(destroyed)
    for planet in sort_destroyed:
        print(f"-> {planet}")
