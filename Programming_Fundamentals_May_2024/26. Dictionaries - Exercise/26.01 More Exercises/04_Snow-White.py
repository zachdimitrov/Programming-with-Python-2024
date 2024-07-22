class Dwarf:
    def __init__(self, name, color, physics):
        self.name = name
        self.color = color
        self.physics = physics
        self.count = 1

    def __repr__(self):
        print(self.name, self.color, self.physics, self.count)

dwarfs = []

while True:
    command = input()
    if command == "Once upon a time":
        break
    line = command.split(" <:> ")
    name = line[0]
    color = line[1]
    physics = int(line[2])

    new_dwarf = Dwarf(name, color, physics)
    if len(dwarfs) > 0:
        found = False
        for dwarf in dwarfs:
            if dwarf.name == new_dwarf.name and dwarf.color == new_dwarf.color:
                if physics > dwarf.physics:
                    dwarf.physics = physics
                found = True
            if dwarf.color == new_dwarf.color:
                dwarf.count += 1
                new_dwarf.count += 1
        if not found:
            dwarfs.append(new_dwarf)
    else:
        dwarfs.append(new_dwarf)

sorted_dwarfs = sorted(dwarfs, key=lambda x: (x.physics, x.count), reverse=True)
for dwarf in sorted_dwarfs:
    print(f"({dwarf.color}) {dwarf.name} <-> {dwarf.physics}")
