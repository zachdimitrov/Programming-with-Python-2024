firstStr = input()
secondStr = input()
mutations = [firstStr]
for i in range(0, len(firstStr)):
    mutation = ''
    for j in range(0, len(firstStr)):
        if j <= i:
            mutation += secondStr[j]
        else:
            mutation += firstStr[j]
    if not mutations.__contains__(mutation):
        mutations.append(mutation)
        print(mutation)
