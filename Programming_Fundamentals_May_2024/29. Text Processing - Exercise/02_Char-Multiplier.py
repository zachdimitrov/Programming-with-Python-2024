strings = input().split(" ")
shortest_length = min(len(strings[0]), len(strings[1]))
total = 0
for i in range(shortest_length):
    code1 = ord(strings[0][i])
    code2 = ord(strings[1][i])
    total = total + code1*code2

longest_string = strings[0]
if len(strings[1]) > len(longest_string):
    longest_string = strings[1]

for k in range(shortest_length, len(longest_string)):
    code3 = ord(longest_string[k])
    total += code3

print(total)
