def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


first = int(input())
second = int(input())

print(f"{factorial(first) / factorial(second):.2f}")
