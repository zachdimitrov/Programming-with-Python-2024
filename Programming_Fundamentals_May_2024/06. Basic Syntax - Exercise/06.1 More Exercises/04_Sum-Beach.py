phrase = input().lower()
found = 0
word = ''
for i in range(0, len(phrase) - 1):
    for j in range(i, i + 5):
        if j <= len(phrase) - 1:
            word += phrase[j]
        else:
            break
        if word == 'sand' or word == 'water' or word == 'fish' or word == 'sun':
            found += 1
            word = ''
            continue
    word = ''
print(found)
