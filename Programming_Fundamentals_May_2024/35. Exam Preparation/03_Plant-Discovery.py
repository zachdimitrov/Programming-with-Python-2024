class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings = []

    def rate(self, new_rating):
        self.ratings.append(new_rating)

    def reset(self):
        self.ratings.clear()

    def __repr__(self):
        avg_rating = 0.00
        if self.ratings:
            avg_rating = sum(self.ratings)/len(self.ratings)
        print(f"- {self.name}; Rarity: {self.rarity}; Rating: {avg_rating:.2f}")


def find_plant(name):
    for p in plants:
        if p.name == name:
            return p


n = int(input())
plants = []
for i in range(n):
    line = input().split("<->")
    name = line[0]
    rarity = int(line[1])
    current = find_plant(name)
    if current:
        current.rarity = rarity
    else:
        plants.append(Plant(name, rarity))

command = input()
while command != "Exhibition":
    line = command.split(": ")
    instr = line[0]
    if instr == "Rate":
        data = line[1].split(" - ")
        name = data[0]
        new_rating = float(data[1])
        plant = find_plant(name)
        if plant:
            plant.rate(new_rating)
        else:
            print("error")
    elif instr == "Update":
        data = line[1].split(" - ")
        name = data[0]
        new_rarity = int(data[1])
        plant = find_plant(name)
        if plant:
            plant.rarity = new_rarity
        else:
            print("error")
    elif instr == "Reset":
        name = line[1]
        plant = find_plant(name)
        if plant:
            plant.reset()
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")
for p in plants:
    p.__repr__()