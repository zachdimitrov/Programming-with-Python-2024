str_list = input().split(" ")
int_list = list(map(int, str_list))
count = int(input())

for i in range(count):
    int_list.remove(min(int_list))

print(*int_list, sep=", ")
