text = input()
seq = []
letters = ""
nums = ""
unique = set()
result = ""
for i in range(0, len(text)):
    if not text[i].isnumeric():
        letters += text[i]
        if i + 1 < len(text) and text[i + 1].isnumeric():
            seq.append(letters)
            letters = ""
    else:
        nums += text[i]
        if i + 1 < len(text) and not text[i + 1].isnumeric():
            seq.append(int(nums))
            nums = ""
        elif i == len(text) - 1:
            seq.append(int(nums))

for j in range(0, len(seq) - 1, 2):
    new_text = seq[j].upper()
    num = seq[j + 1]
    for s in new_text:
        unique.add(s)
    result += new_text*num

print(f"Unique symbols used: {len(unique)}")
print(result)

