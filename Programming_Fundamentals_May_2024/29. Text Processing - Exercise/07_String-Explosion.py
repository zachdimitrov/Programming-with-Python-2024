text = input()
result = ""
strength = 0
for i in range(0, len(text)):
    if text[i] == ">":
        if i < len(text) - 1:
            strength += int(text[i + 1])
        result += text[i]
        continue
    if strength == 0:
        result += text[i]
    if strength > 0:
        strength -= 1
print(result)
