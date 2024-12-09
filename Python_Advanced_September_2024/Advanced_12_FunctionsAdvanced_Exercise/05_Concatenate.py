def concatenate(*args, **kvargs):
    result = ""
    for word in args:
        result += word
    for key, value in kvargs.items():
        if key in result:
            result = result.replace(key, value)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))