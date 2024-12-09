from collections import deque


def boarding_passengers(capacity, *groups):
    programs = {}
    removed_groups = []
    groups_queue = deque(groups)
    while groups_queue:
        group = groups_queue.popleft()
        if capacity <= 0:
            removed_groups.append(group)
            break
        if capacity - group[0] >= 0:
            capacity = capacity - group[0]
            if group[1] not in programs:
                programs[group[1]] = group[0]
            else:
                programs[group[1]] += group[0]
        else:
            removed_groups.append(group)
            continue

    programs = dict(sorted(programs.items(), key=lambda x: (-x[1], x[0])))

    result = f"Boarding details by benefit plan:\n"
    for key, val in programs.items():
        result += f"## {key}: {val} guests\n"
    if len(removed_groups) == 0:
        result += "All passengers are successfully boarded!"
    if capacity == 0 and (len(removed_groups) > 0 or len(groups_queue) > 0):
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    if capacity > 0 and (len(removed_groups) > 0 or len(groups_queue) > 0):
        result += f"Partial boarding completed. Available capacity: {capacity}."
    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print("---------------------------------")
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print("---------------------------------")
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
