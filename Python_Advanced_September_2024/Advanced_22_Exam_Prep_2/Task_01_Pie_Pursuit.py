from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
    current_contestant = contestants[0]
    current_pie = pies[-1]

    if current_contestant >= current_pie:
        remaining_contestant = contestants.popleft() - pies.pop()
        if remaining_contestant > 0:
            contestants.append(remaining_contestant)
    else:
        remaining_pie = pies.pop() - contestants.popleft()
        if remaining_pie > 1:
            pies.append(remaining_pie)
        elif remaining_pie == 1:
            if len(pies) > 1:
                pies[-1] += 1
            else:
                pies.append(1)


if (not pies) and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(x) for x in contestants])}")
if not pies and not contestants:
    print("We have a champion!")
if (not contestants) and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(x) for x in pies])}")