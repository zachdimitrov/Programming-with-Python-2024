word = input()
chars = {}
for c in word:
    if c != " ":
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1


