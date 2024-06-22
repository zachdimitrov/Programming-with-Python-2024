fire_cells = input().split("#")
water = int(input())
effort = 0
cells_out = []
total_fire = 0
is_valid = True
for c in fire_cells:
    cell = c.split(" = ")
    cell_type = cell[0]
    cell_range = int(cell[1])

    if cell_type == "High" and (cell_range < 81 or cell_range > 125):
        is_valid = False
    elif cell_type == "Medium" and (cell_range < 51 or cell_range > 80):
        is_valid = False
    elif cell_type == "Low" and (cell_range < 1 or cell_range > 50):
        is_valid = False

    if is_valid:
        if water >= cell_range:
            water -= cell_range
            total_fire += cell_range
            cells_out.append(cell_range)
            effort += cell_range * 0.25
        else:
            continue
    is_valid = True

print("Cells:")
for elm in cells_out:
    print(f" - {elm}")
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
