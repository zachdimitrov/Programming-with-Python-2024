def key_contains(key, subst):
    if subst in key:
        print(f"{key} contains {subst}")
    else:
        print("Substring not found!")


def change_upper(key, start, end):
    front_part = key[:start]
    back_part = key[end:]
    changed_part = key[start:end].upper()
    return front_part + changed_part + back_part


def change_lower(key, start, end):
    front_part = key[:start]
    back_part = key[end:]
    changed_part = key[start:end].lower()
    return front_part + changed_part + back_part


def key_slice(key, start, end):
    front_part = key[:start]
    back_part = key[end:]
    return front_part + back_part


raw_key = input()
command = input()

while command != "Generate":
    lines = command.split(">>>")
    if lines[0] == "Contains":
        key_contains(raw_key, lines[1])
    elif lines[0] == "Flip":
        if lines[1] == "Upper":
            raw_key = change_upper(raw_key, int(lines[2]), int(lines[3]))
        elif lines[1] == "Lower":
            raw_key = change_lower(raw_key, int(lines[2]), int(lines[3]))
        print(raw_key)
    elif lines[0] == "Slice":
        raw_key = key_slice(raw_key, int(lines[1]), int(lines[2]))
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")
