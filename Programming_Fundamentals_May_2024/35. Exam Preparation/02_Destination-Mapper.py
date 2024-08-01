import re
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
line = input()
length = 0
destinations = []
found = re.findall(pattern, line)
if found:
    for dest in found:
        if dest:
            length += len(dest[1])
            destinations.append(dest[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {length}")
