class Converter:

    @staticmethod
    def decimal_to_binary(data: str):
        binary = ""
        number = int(data)
        while number > 0:
            binary += str(number % 2)
            number = number // 2
        return binary[::-1]

    @staticmethod
    def binary_to_decimal(number: str):
        decimal = 0
        rev_number = number[::-1]
        for i in range(len(rev_number)):
            digit = int(rev_number[i])
            decimal = decimal + (digit * (2 ** i))
        return decimal

    @staticmethod
    def sixteen_to_decimal(number: str):
        decimal = 0
        rev_number = number[::-1]
        for i in range(len(rev_number)):
            digit = rev_number[i].lower()
            res = 0
            if digit == "0" or digit == "1" or \
                digit == "2" or digit == "3" or \
                digit == "4" or digit == "5" or \
                digit == "6" or digit == "7" or \
                digit == "8" or digit == "9":
                res = int(digit)
            elif digit == "a":
                res = 10
            elif digit == "b":
                res = 11
            elif digit == "c":
                res = 12
            elif digit == "d":
                res = 13
            elif digit == "e":
                res = 14
            elif digit == "f":
                res = 15
            decimal = decimal + (res * (16 ** i))
        return decimal

    @staticmethod
    def decimal_to_sixteen(data: str):
        sixteen = ""
        number = int(data)
        while number > 0:
            remain = number % 16
            if 0 <= remain < 10:
                sixteen += str(remain)
            elif remain == 10:
                sixteen += "A"
            elif remain == 11:
                sixteen += "B"
            elif remain == 12:
                sixteen += "C"
            elif remain == 13:
                sixteen += "D"
            elif remain == 14:
                sixteen += "E"
            elif remain == 15:
                sixteen += "F"
            number = number // 16
        return sixteen[::-1]


while True:
    command = input("Select convertion or [E]nd:\n"
          "[B] for binary -> decimal\n"
          "[D] for decimal -> binary\n"
          "[I] for decimal -> hexadecimal\n"
          "[S] for hexadecimal -> decimal\n")
    command = command.lower()
    if command == "e":
        break
    if command == "b":
        number = input("Input binary number (digits 0 and 1 only): ")
        result = Converter.binary_to_decimal(number)
        print(f"{number} bin -> {result} dec")
        restart = input("Start again? [Y][N]")
        if restart.lower() == "n":
            break
    elif command == "d":
        number = input("Input decimal number (digits from 0 to 9 only): ")
        result = Converter.decimal_to_binary(number)
        print(f"{number} dec -> {result} bin")
        restart = input("Start again? [Y][N]")
        if restart.lower() == "n":
            break
    elif command == "i":
        number = input("Input decimal number (digits from 0 to 9 only): ")
        result = Converter.decimal_to_sixteen(number)
        print(f"{number} dec -> {result} hex")
        restart = input("Start again? [Y][N]")
        if restart.lower() == "n":
            break
    elif command == "s":
        number = input("Input hex number (digits 0-9 and letters A-F): ")
        result = Converter.sixteen_to_decimal(number)
        print(f"{number} hex -> {result} dec")
        restart = input("Start again? [Y][N]")
        if restart.lower() == "n":
            break