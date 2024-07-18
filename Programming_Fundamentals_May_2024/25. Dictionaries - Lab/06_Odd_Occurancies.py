words = input().split(" ")
occurancies = {}
for word in words:
    lowercase = word.lower()
    if lowercase not in occurancies:
        occurancies[lowercase] = 0
    occurancies[lowercase] += 1

for key, value in occurancies.items():
    if value % 2 != 0:
        print(key, end=" ")
