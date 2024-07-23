import re
line = input()
word = input()
pattern = r"\b" + word + r"\b"
names = re.findall(pattern, line, re.IGNORECASE)
print(len(names))
