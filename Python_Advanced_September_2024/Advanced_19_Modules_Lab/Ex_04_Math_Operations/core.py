from Advanced_19_Modules_Lab.Ex_04_Math_Operations.errors import UnknownSignError


def sum_nums(num1, num2):
    return num1 + num2


def sub_nums(num1, num2):
    return num1 - num2


def mul_nums(num1, num2):
    return num1 * num2


def div_nums(num1, num2):
    return num1 / num2


def pow_nums(num1, num2):
    return num1 ** num2


mapper = {
    "+": sum_nums,
    "-": sub_nums,
    "*": mul_nums,
    "/": div_nums,
    "^": pow_nums,
}


def execute(num1, sign, num2):
    if sign in mapper:
        resp_function = mapper[sign]
        return resp_function(num1, num2)
    raise UnknownSignError("Please provide correct sign [+-*/^]!")
