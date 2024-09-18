# numbers = [int(el) for el in input().split()]
# target = int(input())
#
# for i in range(len(numbers)):
#     if numbers[i] == '':
#         continue
#     for j in range(i + 1, len(numbers)):
#         if numbers[j] == '':
#             continue
#         if numbers[i] + numbers[j] == target:
#             print(f"{numbers[i]} + {numbers[j]} = {target}")
#             numbers[i] = ''
#             numbers[j] = ''
#             break


numbers = [int(el) for el in input().split()]
target = int(input())

targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value

# test case
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
# 30