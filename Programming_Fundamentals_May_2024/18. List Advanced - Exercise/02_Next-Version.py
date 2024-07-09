current_v = list(map(int, input().split(".")))

if current_v[2] < 9:
    current_v[2] += 1
else:
    current_v[2] = 0
    if current_v[1] < 9:
        current_v[1] += 1
    else:
        current_v[1] = 0
        current_v[0] += 1

print(".".join(list(map(str, current_v))))

