def sorting_cheeses(**args):
    result = ""
    args = dict(sorted(args.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in args.items():
        quantities = sorted(value, reverse=True)
        result += key + "\n"
        for val in quantities:
            result += str(val) + "\n"
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
            Parmigiano=[165, 215],
            Feta=[150, 515],
            Brie=[150, 125],
    )
)
