electrons = int(input())
shells = []
layer = 1

while True:
    electrons_to_add = 2 * (layer ** 2)
    remaining = electrons - electrons_to_add
    if remaining > 0:
        shells.append(electrons_to_add)
        electrons = remaining
        layer += 1
    else:
        shells.append(electrons)
        break

print(shells)

