def age_assignment(*names, **ages):
    names = sorted(names)
    string = ""
    for name in names:
        for letter, age in ages.items():
            if letter in name:
                string += f"{name} is {age} years old.\n"
    return string

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
