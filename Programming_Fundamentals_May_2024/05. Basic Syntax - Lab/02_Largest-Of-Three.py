num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
list_num = [num_1, num_2, num_3]
largest = num_1

for elem in list_num:
    if elem > largest:
        largest = elem
print(largest)
