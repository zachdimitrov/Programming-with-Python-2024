data = input().split()
commands = []


def merge_data(start, end, data_list):
    if start < 0:
        start = 0
    if end >= len(data_list):
        end = len(data_list) - 1
    new_part = "".join(data_list[start:end + 1])
    data_list[start:end + 1] = [new_part]

    return data_list


def divide_data(index, parts, data_list):
    new_part = []
    to_divide = data_list[index]
    parts = len(to_divide)//parts
    for i in range(0, len(to_divide), parts):
        add_to_new_part = ""
        for j in range(0, parts):
            if i + j < len(to_divide):
                add_to_new_part += to_divide[i + j]
        new_part.append(add_to_new_part)
    if len(new_part) > 2 and len(new_part[-1]) < len(new_part[-2]):
        new_part = merge_data(len(new_part) - 2, len(new_part) - 1, new_part)

    data_list[index:index + 1] = new_part

    return data_list


def new_divide_data(index, partitions, data_list):
    element = data_list[index]
    part_length = len(element) // partitions

    divided_parts = []
    start = 0

    for i in range(partitions):
        if i == partitions - 1:
            divided_parts.append(element[start:])
        else:
            divided_parts.append(element[start:start + part_length])
            start += part_length

    data_list[index:index + 1] = divided_parts
    return data_list


while True:
    command = input()
    if command == "3:1":
        break
    commands.append(command)

for c in commands:
    cmd = c.split()
    if cmd[0] == "merge":
        merge_data(int(cmd[1]), int(cmd[2]), data)
    elif cmd[0] == "divide":
        new_divide_data(int(cmd[1]), int(cmd[2]), data)

print(" ".join(data))
