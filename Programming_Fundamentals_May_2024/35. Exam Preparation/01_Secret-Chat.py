message = input()
user_input = input()


def insert_space(index):
    first_part = message[:(index)]
    last_part = message[index:]
    result = first_part + " " + last_part
    print(result)
    return result


def reverse(substring):
    if substring in message:
        index = message.index(substring)
        first_part = message[:index]
        mid_part = substring[::-1]
        last_part = message[(index + len(substring)):]
        result = first_part + mid_part + last_part
        print(result)
        return result
    else:
        print("error")
        return message


def change_all(substring, replacement):
    result = message
    while substring in result:
        result = result.replace(substring, replacement)
        print(result)
        return result


while user_input != "Reveal":
    line = user_input.split(":|:")
    command = line[0]
    if command == "InsertSpace":
        index = int(line[1])
        message = insert_space(index)
    elif command == "Reverse":
        message = reverse(line[1])
    elif command == "ChangeAll":
        message = change_all(line[1], line[2])

    user_input = input()

print(f"You have a new text message: {message}")
