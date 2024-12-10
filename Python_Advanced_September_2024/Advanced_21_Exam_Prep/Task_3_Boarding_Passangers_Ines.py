def boarding_passengers(ship_capacity, *passenger_list):
    program_data = {}
    total_boarded = 0
    total_to_board = sum([x[0] for x in passenger_list])

    for passenger_group in passenger_list:
        if ship_capacity == 0:
            break
        count, group_name = passenger_group

        if count <= ship_capacity:
            if group_name not in program_data:
                program_data[group_name] = 0
            program_data[group_name] += count
            total_boarded += count
            ship_capacity -= count

    sorted_data = sorted(program_data.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = "Boarding details by benefit plan:\n"
    for group_name, total_number in sorted_data:
        result += f"## {group_name}: {total_number} guests\n"

    if ship_capacity <= 0 and total_boarded < total_to_board:
        result += "Boarding unsuccessful. Cruise ship at full capacity."

    if ship_capacity >= 0 and total_boarded == total_to_board:
        result += "All passengers are successfully boarded!"

    if ship_capacity != 0 and total_boarded < total_to_board:
        result += f"Partial boarding completed. Available capacity: {ship_capacity}."

    return result


print(boarding_passengers(150,
                          (35, 'Diamond'),
                          (55, 'Platinum'),
                          (35, 'Gold'),
                          (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'),
                          (15, 'Platinum'),
                          (25, 'Gold'),
                          (25, 'First Cruiser'),
                          (15, 'Diamond'),
                          (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'),
                          (20, 'Platinum'),
                          (30, 'Diamond'),
                          (10, 'First Cruiser'),
                          (31, 'Platinum'),
                          (20, 'Diamond')))
