class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LEN = 5
TLS_NAMES = [".com", ".bg", ".org", ".net"]
while True:
    user_input = input()
    if user_input == "End":
        break
    if "@" not in user_input:
        raise MustContainAtSymbolError("Email must contain @")
    username, domain = [x[::-1] for x in user_input[::-1].split('@', 1)][::-1]
    # magic to split by last @ only (reverse -> split by 1-st delimiter -> reverse again)
    print(username, domain)
    if len(username) < MIN_NAME_LEN:
        raise NameTooShortError("Name must be more than 4 characters")
    _, tls = [x[::-1] for x in user_input[::-1].split('.', 1)][::-1]
    # magic to split by last . only
    print(_, tls)
    if f".{tls}" not in TLS_NAMES:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
