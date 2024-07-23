first_char = input()
last_char = input()
seq = input()
result = 0

start_ord = ord(first_char)
end_ord = ord(last_char)

for c in seq:
    current_ord = ord(c)
    if start_ord < current_ord < end_ord:
        result += current_ord

print(result)