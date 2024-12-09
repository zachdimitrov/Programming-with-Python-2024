from collections import deque
parents = deque([*input()])
balanced = True
counter = 0

#85 points solution - wrong, no case for {}[]()
# if len(parents) % 2 != 0:
#     balanced = False
# else:
#     for i in range(0, len(parents)//2):
#         if len(parents) >= 2:
#             first = parents.popleft()
#             last = parents.pop()
#             if first == "(":
#                 if last != ")":
#                     balanced = False
#             elif first == "[":
#                 if last != "]":
#                     balanced = False
#             elif first == "{":
#                 if last != "}":
#                     balanced = False
#         else:
#             balanced = False

opens = ["(", "[", "{"]
closed = [")", "]", "}"]

# for k in range(len(opens)):
#     stack = []
#     print(f"symbol = {opens[k]}, {closed[k]}")
#     for i in range(len(parents)):
#         if parents[i] == opens[k]:
#             stack.append(i)
#         elif parents[i] == closed[k]:
#             if stack:
#                 print([stack, i+1])
#                 start_index = stack.pop()
#                 print(parents[start_index:i + 1])
#                 if len(parents[start_index:i + 1]) % 2 != 0:
#                     balanced = False
#             else:
#                 balanced = False
if len(parents) % 2 != 0:
    balanced = False
else:
    while len(parents):
        #print(parents)
        first_el = parents.popleft()
        next_el = parents.popleft()
        #print("elements: ", first_el, next_el)
        if first_el == opens[0]:
            if next_el == closed[0]:
                counter = 0
                continue
            else:
                parents.appendleft(next_el)
                parents.append(first_el)
        elif first_el == opens[1]:
            if next_el == closed[1]:
                counter = 0
                continue
            else:
                parents.appendleft(next_el)
                parents.append(first_el)
        elif first_el == opens[2]:
            if next_el == closed[2]:
                counter = 0
                continue
            else:
                parents.appendleft(next_el)
                parents.append(first_el)
        else:
            parents.appendleft(next_el)
            parents.append(first_el)

        counter += 1

        if counter == len(parents):
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
