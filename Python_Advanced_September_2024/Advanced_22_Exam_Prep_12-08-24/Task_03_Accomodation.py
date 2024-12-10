from collections import deque

def accommodate(*guests, **rooms):
    accomodations = {}
    rooms_by_number = {}
    accomodated = 0
    filled_rooms = 0
    for num, capacity in rooms.items():
        number_only = int(num.split("_")[1])
        rooms_by_number[number_only] = capacity
    guest_groups = deque(guests)
    sorted_rooms = dict(sorted(rooms_by_number.items(), key=lambda x: (x[1], x[0])))

    while True:
        if len(guest_groups) <= 0:
            break
        current_group = guest_groups.popleft()
        for room, capacity in sorted_rooms.items():
            if capacity >= current_group:
                if room not in accomodations.keys():
                    accomodations[room] = current_group
                    accomodated += current_group
                    filled_rooms += 1
                    break

    not_accomodated = sum(guests) - accomodated
    sorted_accomodations = dict(sorted(accomodations.items(), key=lambda x: x[0]))
    result = ""
    if filled_rooms:
        result += f"A total of {filled_rooms} accommodations were completed!\n"
        for room, guests in sorted_accomodations.items():
            result += f"<Room {room} accommodates {guests} guests>\n"
    else:
        result += "No accommodations were completed!\n"
    if not_accomodated > 0:
        result += f"Guests with no accommodation: {not_accomodated}\n"
    if len(accomodations) < len(sorted_rooms):
        difference = len(sorted_rooms) - len(accomodations)
        result += f"Empty rooms: {difference}"

    return result


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print("..............")
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print("..............")
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))

