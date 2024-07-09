initial_string = input()
numbers_list = []
letters_list = [*initial_string]

for c in initial_string:
    if c.isnumeric():
        letters_list.remove(c)
        numbers_list.append(int(c))

take_list = []
skip_list = []

for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

take_string = []
index = 0
j = 0

while True:
    if index >= len(letters_list):
        break
    take_string += letters_list[index:index + take_list[j]]
    index += take_list[j]
    if j + 1 >= len(skip_list):
        break
    index += skip_list[j]
    j += 1

print("".join(take_string))

