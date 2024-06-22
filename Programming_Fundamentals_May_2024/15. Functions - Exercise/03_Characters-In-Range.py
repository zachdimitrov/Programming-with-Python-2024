def chars_in_range(a, b):
    start = ord(a)
    end = ord(b)
    all_chars = []

    for i in range(start + 1, end):
        all_chars.append(chr(i))

    print(*all_chars, sep=" ")


first = input()
second = input()
chars_in_range(first, second)
