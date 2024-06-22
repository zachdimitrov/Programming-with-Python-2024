def validate_pass(password):
    num_digits = 0
    result = []
    if 6 > len(password) or len(password) > 10:
        result.append("Password must be between 6 and 10 characters")
    for c in password:
        if 47 <= ord(c) <= 57:
            num_digits += 1
        if (47 > ord(c) or ord(c) > 57) and (65 > ord(c) or ord(c) > 90) and (97 > ord(c) or ord(c) > 122):
            message = "Password must consist only of letters and digits"
            if message not in result:
                result.append(message)
    if num_digits < 2:
        result.append("Password must have at least 2 digits")

    if len(result) == 0:
        return ["Password is valid"]
    else:
        return result


print(*validate_pass(input()), sep="\n")
