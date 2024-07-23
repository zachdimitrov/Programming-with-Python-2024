keys = list(map(int, input().split()))
while True:
    command = input()
    if command == "find":
        break
    result = ""
    j = 0
    for i in range(len(command)):
        if j >= len(keys):
            j = 0
        result = result + chr(ord(command[i]) - keys[j])
        j += 1
    type_indexes = []
    pos_indexes = []
    for k in range(len(result)):
        if result[k] == "&":
            type_indexes.append(k)
        elif result[k] == "<" or result[k] == ">":
            pos_indexes.append(k)

    mat_type = result[type_indexes[0] + 1:type_indexes[1]]
    mat_pos = result[pos_indexes[0] + 1:pos_indexes[1]]

    print(f"Found {mat_type} at {mat_pos}")
