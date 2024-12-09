def fill_the_box(height, length, width, *args):
    volume = height * length * width
    filled = 0
    for i in range(len(args)):
        num = args[i]
        if num == "Finish":
            if filled < volume:
                return f"There is free space in the box. You could put {volume - filled} more cubes."
            if filled == volume:
                return f"No more free space! You have 0 more cubes."
        else:
            if filled + num <= volume:
                filled += num
            else:
                rest = num - volume + filled
                return f"No more free space! You have {rest + sum(args[i + 1:-1])} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
