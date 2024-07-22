text = input()
processed = ""
for c in text:
    new_char = chr(ord(c) + 3)
    processed += new_char
print(processed)
