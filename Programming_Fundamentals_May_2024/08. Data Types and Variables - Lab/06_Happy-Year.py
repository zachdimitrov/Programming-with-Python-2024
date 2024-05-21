current = int(input())
next_year = current + 1
while True:
    digits = str(next_year)
    # if len(set(digits) == len(next_year)):
    #     break
    is_special = True
    for i in range(0, len(digits) - 1):
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:
                is_special = False
    if is_special:
        print(next_year)
        break
    next_year += 1
