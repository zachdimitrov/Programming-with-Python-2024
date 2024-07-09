room_number = int(input())
free_chairs = 0
are_free = True
for i in range(1, room_number + 1):
    room = input().split(" ")
    chairs = len(room[0])
    people = int(room[1])
    if chairs < people:
        print(f"{people - chairs} more chairs needed in room {i}")
        are_free = False
    else:
        free_chairs = free_chairs + (chairs - people)

if are_free:
    print(f"Game On, {free_chairs} free chairs left")

