import re
line = input()
pattern = r"(?<= _)[A-Za-z0-9]+\b"
names = re.findall(pattern, line)
print(",".join(names))
