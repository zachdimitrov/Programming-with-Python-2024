import re

def make_upper(password, index):
    first_part = password[:index]
    char = password[index].upper()
    last_part = password[index + 1:]
    return first_part + char + last_part

def make_lower(password, index):
    first_part = password[:index]
    char = password[index].lower()
    last_part = password[index + 1:]
    return first_part + char + last_part


def insert_char(password, index, char):
    first_part = password[:index]
    last_part = password[index:]
    return first_part + char + last_part


def replace_char(password, char, value):
    current_value = ord(char)
    new_char = chr(current_value + value)
    result = password.replace(char, new_char)
    return result


def validation(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    match = re.match(r"\w+", password)
    if match:
        match_group = match.group(0)
        if match_group != password:
            print("Password must consist only of letters, digits and _!")
    else:
        print("Password must consist only of letters, digits and _!")
    lower_pass = password.lower()
    if lower_pass == password:
        print("Password must consist at least one uppercase letter!")
    upper_pass = password.upper()
    if upper_pass == password:
        print("Password must consist at least one lowercase letter!")
    contains_digit = False
    for c in password:
        if c.isdigit():
            contains_digit = True
    if not contains_digit:
        print("Password must consist at least one digit!")


password = input()
while True:
    command = input()
    if command == "Complete":
        break
    line = command.split(" ")
    if line[0] == "Make":
        index = int(line[2])
        if len(password) > index:
            if line[1] == "Upper":
                password = make_upper(password, index)
                print(password)
            elif line[1] == "Lower":
                password = make_lower(password, index)
                print(password)
    elif line[0] == "Insert":
        index = int(line[1])
        if len(password) > index:
            char = line[2]
            password = insert_char(password, index, char)
            print(password)
    elif line[0] == "Replace":
        char = line[1]
        if char in password:
            value = int(line[2])
            password = replace_char(password, char,  value)
            print(password)
    elif line[0] == "Validation":
        validation(password)

