def increase_decrease(dist, element):
    for i in range(len(dist)):
        if dist[i] <= element:
            dist[i] += element
        else:
            dist[i] -= element


def process_index(dist, index):
    val = 0
    if index >= len(dist):
        index = len(dist) - 1
        element = dist[index]
        val = element
        dist.pop(index)
        dist.append(dist[0])
        increase_decrease(dist, element)
    elif index < 0:
        index = 0
        element = dist[index]
        val = element
        dist.pop(index)
        dist.insert(0, dist[-1])
        increase_decrease(dist, element)
    else:
        element = dist[index]
        val = element
        dist.pop(index)
        increase_decrease(dist, element)

    return val


distances = list(map(int, input().split()))
indexes = []
value = 0

while True:
    if len(distances) <= 0:
        break
    next_index = int(input())
    value += process_index(distances, next_index)
print(value)
