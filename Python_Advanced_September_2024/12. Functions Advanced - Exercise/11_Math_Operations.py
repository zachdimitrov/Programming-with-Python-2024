def math_operations(*args, **kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs["a"] += args[i]
        elif i % 4 == 1:
            kwargs["s"] -= args[i]
        elif i % 4 == 2:
            if args[i] != 0:
                kwargs["d"] /= args[i]
        else:
            kwargs["m"] *= args[i]

    result = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    return "\n".join([f"{x}: {y:.1f}" for x,y in result.items()])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
