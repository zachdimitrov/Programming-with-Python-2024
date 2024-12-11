def plant_garden(available_space, *plot_sizes, **plant_types):
    plot_size_for_plant = {}
    for plant, size in plot_sizes:
        if plant not in plot_size_for_plant:
            plot_size_for_plant[plant] = size

    allowed_plants = {}
    for plant, count in plant_types.items():
        if plant in plot_size_for_plant:
            if plant not in allowed_plants:
                allowed_plants[plant] = count

    sorted_allowed_plants = sorted(allowed_plants.items(), key=lambda x: x[0])
    planted_plants = {}
    space_needed = 0
    space_occupied = 0

    for p, count in sorted_allowed_plants:
        space_needed += plot_size_for_plant[p] * count

    for p, count in sorted_allowed_plants:
        space_for_plant = plot_size_for_plant[p]
        if available_space < space_for_plant:
            continue
        if space_for_plant * count <= available_space:
            total_space = space_for_plant * count
            available_space -= total_space
            space_occupied += total_space
            planted_plants[p] = count
        else:
            while available_space >= space_for_plant:
                available_space -= space_for_plant
                space_needed += space_for_plant
                if p not in planted_plants:
                    planted_plants[p] = 0
                planted_plants[p] += 1

    result = ""
    if space_needed == space_occupied:
        result += f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n"
    if space_needed > space_occupied:
        result += "Not enough space to plant all requested plants!\n"
    result += "Planted plants:\n"
    for p, pieces in planted_plants.items():
        result += f"{p}: {pieces}\n"

    return result


print("-------------- TEST --------------\n")

print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
