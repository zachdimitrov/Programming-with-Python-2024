from collections import deque

queue = deque()
liters = int(input())

command = input()
while command != "Start":
    queue.append(command)
    command = input()

new_command = input().split()
while new_command[0] != "End":
    if new_command[0] == "refill":
        liters += int(new_command[1])
    else:
        needed = int(new_command[0])
        person = queue.popleft()
        if liters >= needed:
            print(f"{person} got water")
            liters -= needed
        else:
            print(f"{person} must wait")
    new_command = input().split()

print(f"{liters} liters left")
