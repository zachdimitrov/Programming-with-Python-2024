from collections import deque

queue = deque()
command = input()
while command != "End":
    if command != "Paid":
        queue.append(command)
    else:
        while len(queue) > 0:
            print(queue.popleft())
    command = input()
print(f"{len(queue)} people remaining.")
