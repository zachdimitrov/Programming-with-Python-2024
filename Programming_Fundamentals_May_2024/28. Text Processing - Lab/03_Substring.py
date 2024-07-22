sub = input()
main = input()
result = main.replace(sub, "")
while True:
    if sub not in result:
        break
    result = result.replace(sub, "")
print(result)
