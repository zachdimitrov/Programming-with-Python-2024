import re


class Food:
    def __init__(self, name, date, calories):
        self.name = name
        self.date = date
        self.calories = calories

    def __repr__(self):
        print(f"Item: {self.name}, Best before: {self.date}, Nutrition: {self.calories}")


pattern = r"([#\|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
line = input()
foods = []
all_calories = 0
found = re.findall(pattern, line)
if found:
    for group in found:
        if group:
            name = group[1]
            date = group[2]
            calories = int(group[3])
            foods.append(Food(name, date, calories))
            all_calories += calories

print(f"You have food to last you for: {all_calories // 2000} days!")
for f in foods:
    f.__repr__()
