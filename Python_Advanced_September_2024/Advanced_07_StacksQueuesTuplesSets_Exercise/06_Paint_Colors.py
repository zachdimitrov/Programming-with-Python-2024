sublist = input().split()
main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
colors = []

while len(sublist) > 0:
    first = sublist[0]
    sublist.remove(sublist[0])
    if len(sublist) >= 1:
        last = sublist[-1]
        sublist.remove(sublist[-1])
    else:
        last = ""

    if first + last in main or first + last in secondary:
        colors.append(first + last)
    elif last + first in main or last + first in secondary:
        colors.append(last + first)
    else:
        first = first[:-1]
        last = last[:-1]
        position = len(sublist)//2
        sublist[position:position] = [first, last]
        sublist = [x for x in sublist if x]

for color in colors:
    if color in secondary:
        if color == "orange":
            if not ("red" in colors and "yellow" in colors):
                colors.remove("orange")
        elif color == "purple":
            if not ("red" in colors and "blue" in colors):
                colors.remove("purple")
        elif color == "green":
            if not ("yellow" in colors and "blue" in colors):
                colors.remove("green")
print(colors)
