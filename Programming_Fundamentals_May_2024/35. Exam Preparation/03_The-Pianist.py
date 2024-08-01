class Piece:
    def __init__(self, name, composer, key):
        self.name = name
        self.composer = composer
        self.key = key

    def change_key(self, new_key):
        self.key = new_key

    def __repr__(self):
        print(f"{self.name} -> Composer: {self.composer}, Key: {self.key}")


def find_piece(name):
    for p in pieces:
        if p.name == name:
            return p


n = int(input())
pieces = []

for i in range(n):
    initial = input().split("|")
    name = initial[0]
    composer = initial[1]
    key = initial[2]
    pieces.append(Piece(name, composer, key))

command = input()
while command != "Stop":
    line = command.split("|")
    inst = line[0]
    name = line[1]
    if inst == "Add":
        if find_piece(name):
            print(f"{name} is already in the collection!")
        else:
            composer = line[2]
            key = line[3]
            pieces.append(Piece(name, composer, key))
            print(f"{name} by {composer} in {key} added to the collection!")
    elif inst == "Remove":
        piece_to_remove = find_piece(name)
        if piece_to_remove:
            pieces.remove(piece_to_remove)
            print(f"Successfully removed {name}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")
    elif inst == "ChangeKey":
        new_key = line[2]
        piece_to_update = find_piece(name)
        if piece_to_update:
            piece_to_update.change_key(new_key)
            print(f"Changed the key of {name} to {new_key}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")

    command = input()

for piece in pieces:
    piece.__repr__()
