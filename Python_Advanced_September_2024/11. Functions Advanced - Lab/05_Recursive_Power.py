def recursive_power(number, power):
    if power == 1:
        return number
    else:
        return recursive_power(number, power - 1) * number


print(recursive_power(2, 10))
print(recursive_power(10, 100))
