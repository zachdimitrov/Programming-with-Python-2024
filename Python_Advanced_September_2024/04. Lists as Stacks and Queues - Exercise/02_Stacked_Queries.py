from math import inf


def print_max(s):
    print(max(s))
    # temp_stack = []
    # max_elem = -inf
    # while len(s) > 0:
    #     elem = s.pop()
    #     temp_stack.append(elem)
    #     if elem > max_elem:
    #         max_elem = elem
    # while len(temp_stack) > 0:
    #     s.append(temp_stack.pop())
    #
    # print(max_elem)


def print_min(s):
    print(min(s))
    # temp_stack = []
    # min_elem = inf
    # while len(s) > 0:
    #     elem = s.pop()
    #     temp_stack.append(elem)
    #     if elem < min_elem:
    #         min_elem = elem
    # while len(temp_stack) > 0:
    #     s.append(temp_stack.pop())
    #
    # print(min_elem)


number = int(input())
stack = []
for i in range(number):
    command = input().split()
    if command[0] == "1":
        number = int(command[1])
        stack.append(number)
    elif command[0] == "2" and len(stack) > 0:
        stack.pop()
    elif command[0] == "3" and len(stack) > 0:
        print_max(stack)
    elif command[0] == "4" and len(stack) > 0:
        print_min(stack)

while len(stack) > 1:
    print(stack.pop(), end=", ")
print(stack.pop())
