def even_odd_filter(**kvargs):
    # for key, value in kvargs.items():
    #     if key == "odd":
    #         kvargs[key] = [x for x in value if x % 2 != 0]
    #     else:
    #         kvargs[key] = [x for x in value if x % 2 == 0]

    kvargs = {key: [x for x in value if x % 2 == (0 if key == "even" else 1)]
              for key, value in kvargs.items()}

    return dict(sorted(kvargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
print(even_odd_filter(
    odd=[0, 9, 9],
    even=[0],
))