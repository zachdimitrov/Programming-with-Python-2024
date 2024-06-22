code = input().split(" ")
message = [*input()]
result = []

for elm in code:
    numbers = list(map(int, [*elm]))
    i = sum(numbers)
    while i >= len(message):
        i = i - len(message)
    result.append(message[i])
    message.pop(i)

print(*result, sep="")
