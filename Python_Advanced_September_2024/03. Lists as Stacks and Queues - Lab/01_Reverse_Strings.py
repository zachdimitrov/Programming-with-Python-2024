text = list(input())
result = []
for i in range(len(text)):
    result.append(text.pop())
print("".join(result))
