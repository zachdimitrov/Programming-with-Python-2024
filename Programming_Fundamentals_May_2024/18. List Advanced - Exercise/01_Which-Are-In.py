first_seq = input().split(", ")
second_seq = input().split(", ")
result = []

for word in first_seq:
    for x in second_seq:
        if word in x:
            if word not in result:
                result.append(word)

print(result)

