def move_letters(num):
    front_part = message[:num]
    back_part = message[num:]
    return back_part + front_part


def insert_to(index, value):
    front_part = message[:index]
    back_part = message[index:]
    return front_part + value + back_part


def change_all(substring, replacement):
    result = message
    while substring in result:
        result = result.replace(substring, replacement)
        return result


message = input()
command = input()
while command != "Decode":
    line = command.split("|")
    task = line[0]
    if task == "Move":
        num_letters = int(line[1])
        message = move_letters(num_letters)
    elif task == "Insert":
        index = int(line[1])
        value = line[2]
        message = insert_to(index, value)
    elif task == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        message = change_all(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
