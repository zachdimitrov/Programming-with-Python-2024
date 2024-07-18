chars = input().split(", ")
characters = {}
for item in chars:
    characters[item] = ord(item)
print(characters)
