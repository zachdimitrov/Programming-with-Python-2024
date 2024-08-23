line = input().split()
stack = []
for i in range(len(line)):
    stack.append(line[i])

for i in range(len(stack)):
    print(stack.pop(), end=" ")
