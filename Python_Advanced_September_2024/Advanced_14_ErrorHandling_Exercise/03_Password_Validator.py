class PasswordTooShortException(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


PASS_MIN_LENGTH = 8
SPECIAL_CHARS = ["@", "*", "&", "%"]
while True:
    password = input()
    if password == "Done":
        break
    if len(password) < PASS_MIN_LENGTH:
        raise PasswordTooShortException("Password must contain at least 8 characters")
    if password.isalpha() or password.isdigit() or all(c in SPECIAL_CHARS for c in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    if not any(c in SPECIAL_CHARS for c in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    print("Password is valid")
