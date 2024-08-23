clothes = [int(x) for x in input().split()]
initial_capacity = int(input())

racks = 1
capacity = initial_capacity

while len(clothes):
    piece = clothes.pop()
    if capacity < piece:
        racks += 1
        capacity = initial_capacity
    capacity -= piece

print(racks)
