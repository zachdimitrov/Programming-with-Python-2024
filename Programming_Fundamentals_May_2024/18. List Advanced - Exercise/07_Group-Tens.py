num_list = list(map(int, input().split(", ")))

for i in range(10, max(num_list) + 10, 10):
    print(f"Group of {i}'s: {[e for e in num_list if i - 10 < e <= i]}")
