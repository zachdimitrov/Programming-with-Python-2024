import math


def exchange(lst, i):
    if 0 > i or i >= len(lst):
        return "Invalid index"
    first = lst[0:i + 1]
    second = lst[i + 1:]
    return second + first


def max_even_odd(lst, cmd):
    if cmd == "even":
        max_even = -math.inf
        max_even_index = -1
        for elm in lst:
            if elm % 2 == 0 and elm >= max_even:
                max_even = elm
                max_even_index = lst.index(elm)
        if max_even_index >= 0:
            return max_even_index
    elif cmd == "odd":
        max_odd = -math.inf
        max_odd_index = -1
        for elm in lst:
            if elm % 2 != 0 and elm >= max_odd:
                max_odd = elm
                max_odd_index = lst.index(elm)
        if max_odd_index >= 0:
            return max_odd_index

    return "No matches"


def min_even_odd(lst, cmd):
    if cmd == "even":
        min_even = math.inf
        min_even_index = -1
        for elm in lst:
            if elm % 2 == 0 and elm <= min_even:
                min_even = elm
                min_even_index = lst.index(elm)
        if min_even_index >= 0:
            return min_even_index
    elif cmd == "odd":
        min_odd = math.inf
        min_odd_index = -1
        for elm in lst:
            if elm % 2 != 0 and elm <= min_odd:
                min_odd = elm
                min_odd_index = lst.index(elm)
        if min_odd_index >= 0:
            return min_odd_index

    return "No matches"


def first_count(lst, count, cmd):
    res = []
    if count > len(lst):
        return "Invalid count"
    if cmd == "even":
        for elm in lst:
            if elm % 2 == 0:
                res.append(elm)
        if len(res) > count:
            return res[:count]
        else:
            return res
    elif cmd == "odd":
        for elm in lst:
            if elm % 2 != 0:
                res.append(elm)
        if len(res) > count:
            return res[:count]
        else:
            return res
    else:
        return res


def last_count(lst, count, cmd):
    res = []
    if count > len(lst):
        return "Invalid count"
    if cmd == "even":
        for elm in lst:
            if elm % 2 == 0:
                res.append(elm)
        if len(res) > count:
            return res[-count:]
        else:
            return res
    elif cmd == "odd":
        for elm in lst:
            if elm % 2 != 0:
                res.append(elm)
        if len(res) > count:
            return res[-count:]
        else:
            return res
    else:
        return res


list_read = list(map(int, input().split(" ")))
command_str = input()

while command_str != "end":
    command = command_str.split(" ")
    # print(command)
    if command[0] == "exchange":
        result = exchange(list_read, int(command[1]))
        if isinstance(result, list):
            list_read = result
        else:
            print(result)
    elif command[0] == "max":
        print(max_even_odd(list_read, command[1]))
    elif command[0] == "min":
        print(min_even_odd(list_read, command[1]))
    elif command[0] == "first":
        result = first_count(list_read, int(command[1]), command[2])
        print(result)
    elif command[0] == "last":
        result = last_count(list_read, int(command[1]), command[2])
        print(result)
    else:
        continue

    command_str = input()

print(list_read)
