def list_roman_emperors(*successes, **rule_lengths):
    is_successful = {}
    successful = {}
    unsuccessful = {}

    for s in successes:
        is_successful[s[0]] = s[1]

    for emperor, years in rule_lengths.items():
        if is_successful[emperor]:
            successful[emperor] = years
        else:
            unsuccessful[emperor] = years

    sorted_successful = dict(sorted(successful.items(), key=lambda x: (-x[1], x[0])))
    sorted_unsuccessful = dict(sorted(unsuccessful.items(), key=lambda x: (x[1], x[0])))

    result = f"Total number of emperors: {len(successful) + len(unsuccessful)}\n"
    if successful:
        result += "Successful emperors:\n"
        for emp, years in sorted_successful.items():
            result += f"****{emp}: {years}\n"
    if unsuccessful:
        result += "Unsuccessful emperors:\n"
        for emp, years in sorted_unsuccessful.items():
            result += f"****{emp}: {years}\n"
    return result

print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False),
                              ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4,
                              Pertinax=4, Vespasian=19, ))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19,
                              Claudius=13, ))
