start_letter = input()
end_letter = input()
removed = input()
combinations = 0
first_sb = ''
second_sb = ''
third_sb = ''

for i in range(ord(start_letter), ord(end_letter) + 1):
    if i != ord(removed):
        first_sb = chr(i)
    else:
        continue
    for j in range(ord(start_letter), ord(end_letter) + 1):
        if j != ord(removed):
            second_sb = chr(j)
        else:
            continue
        for k in range(ord(start_letter), ord(end_letter) + 1):
            if k != ord(removed):
                third_sb = chr(k)
                print(first_sb + second_sb + third_sb + ' ', end='')
                combinations += 1
            else:
                continue

print(combinations)
