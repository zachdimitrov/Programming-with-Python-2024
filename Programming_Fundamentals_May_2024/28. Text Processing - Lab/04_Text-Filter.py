banned = input().split(", ")
text = input()

for word in banned:
    length = len(word)
    while word in text:
        text = text.replace(word, f"{'*'*len(word)}")

print(text)
