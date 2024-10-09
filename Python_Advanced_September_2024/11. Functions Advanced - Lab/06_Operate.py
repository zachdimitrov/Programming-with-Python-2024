from functools import reduce


def operate(operator, *args):

    def addition():
        return reduce(lambda x, y: x + y, args)
        # result = 0
        # for num in args:
        #     result += num
        # return result

    def subtraction():
        return reduce(lambda x, y: x - y, args)
        # result = 0
        # for num in args:
        #     result -= num
        # return result

    def multiplication():
        return reduce(lambda x, y: x * y, args)
        # result = 1
        # for num in args:
        #     result *= num
        # return result

    def division():
        return reduce(lambda x, y: x / y, args)
        # result = args[0]
        # for i in range(1, len(args)):
        #     if args[i] != 0:
        #         result /= args[i]
        #     else:
        #         return None
        # return result

    mapper = {"+": addition, "-": subtraction, "*": multiplication, "/": division}
    return mapper[operator]()

    # if operator == "+":
    #     return addition()
    # elif operator == "-":
    #     return subtraction()
    # elif operator == "*":
    #     return multiplication()
    # elif operator == "/":
    #     return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 5, 1, 6, 2, 1))
