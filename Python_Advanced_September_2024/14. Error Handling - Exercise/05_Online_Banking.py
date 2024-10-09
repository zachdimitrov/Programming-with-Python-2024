class MoneyNotEnoughError (Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


MIN_AGE = 18
pin, money, age = input().split(", ")
money = float(money)
age = int(age)

while True:
    commands = input()
    if commands == "End":
        break
    details = commands.split("#")
    if details[0] == "Send Money":
        money_to_send, try_pin = float(details[1]), details[2]
        if age < MIN_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        if try_pin != pin:
            raise PINCodeError("Invalid PIN code")
        if money_to_send <= money:
            money -= money_to_send
            print(f"Successfully sent {money_to_send} money to a friend")
            print(f"There is {money:.2f} money left in the bank account")
        else:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
    elif details[0] == "Receive Money":
        received_money = float(details[1])
        if received_money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        else:
            money += received_money / 2
            print(f"{received_money / 2:.2f} money went straight into the bank account")
