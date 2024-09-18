from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
value = int(input())

bullets_cost = 0
barrel_used = 0
current_lock = locks.popleft()
unlocked = False

while bullets:
    if barrel_used >= barrel_size:
        print("Reloading!")
        barrel_used = 0
    bullet = bullets.pop()
    barrel_used += 1
    bullets_cost += bullet_price

    if bullet <= current_lock:
        print("Bang!")
        if locks:
            current_lock = locks.popleft()
        else:
            if bullets and barrel_used >= barrel_size:
                print("Reloading!")
            unlocked = True
            break
    else:
        print("Ping!")

if not unlocked:
    locks.append(current_lock)

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullets_count = 0
    if bullets:
        bullets_count = len(bullets)
    print(f"{bullets_count} bullets left. Earned ${value - bullets_cost}")
