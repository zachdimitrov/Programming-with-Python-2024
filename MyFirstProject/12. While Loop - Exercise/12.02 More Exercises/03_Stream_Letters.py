result = ''
word = ''
seen_o = False
seen_n = False
seen_c = False

while True:
    command = input()
    if command == 'End':
        print(result)
        break
    else:
        if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
            if command == 'o' and (not seen_o):
                seen_o = True
            elif command == 'c' and (not seen_c):
                seen_c = True
            elif command == 'n' and (not seen_n):
                seen_n = True
            else:
                word = word + command
        if seen_o and seen_c and seen_n:
            seen_o = False
            seen_n = False
            seen_c = False
            result = result + word + ' '
            word = ''

