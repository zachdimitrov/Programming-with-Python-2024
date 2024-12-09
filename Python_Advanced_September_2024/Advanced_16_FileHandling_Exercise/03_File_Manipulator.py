import os

ABSTRACT_PATH = os.path.abspath("")

while True:
    command = input()
    if command == "End":
        break
    rules = command.split("-")
    name = rules[1]
    file_path = os.path.join(ABSTRACT_PATH, "03_File_Manipulator_Files", name)
    if rules[0] == "Create":
        with open(file_path, "w") as file:
            file.write("")
    elif rules[0] == "Add":
        content = rules[2]
        with open(file_path, "a") as file:
            file.write(content + "\n")
    elif rules[0] == "Replace":
        old_str = rules[2]
        new_str = rules[3]
        try:
            with open(file_path) as file:
                text = file.read()
                replaced = text.replace(old_str, new_str)
            with open(file_path, "w") as file:
                file.write(replaced)
        except FileNotFoundError:
            print("An error occurred")
    elif rules[0] == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")
