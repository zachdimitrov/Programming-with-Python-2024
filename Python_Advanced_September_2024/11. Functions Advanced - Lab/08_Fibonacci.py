def fibonacci(n, memo={0: 0, 1: 1}):
    if not n in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


for i in range(1, 100):
    print(fibonacci(i), end=", ")
