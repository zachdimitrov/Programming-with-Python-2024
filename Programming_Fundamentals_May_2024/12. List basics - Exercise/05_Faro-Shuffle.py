deck = input().split(" ")
shuffles = int(input())


def faro_shuffle(d):
    half_deck = len(d) // 2
    shuffled = []
    for i in range(0, half_deck):
        shuffled.append(d[i])
        shuffled.append(d[half_deck + i])
    return shuffled


# print(deck)

for i in range(shuffles):
    deck = faro_shuffle(deck)

print(deck)
