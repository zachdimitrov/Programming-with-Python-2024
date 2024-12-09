num = int(input())
longest_intersection = set()

for _ in range(num):
    all_intervals = input().split("-")
    first_interval = (int(all_intervals[0].split(",")[0]), int(all_intervals[0].split(",")[1]))
    second_interval = (int(all_intervals[1].split(",")[0]), int(all_intervals[1].split(",")[1]))
    #print(first_interval, second_interval)
    first_set = set()
    for i in range(first_interval[0], first_interval[1] + 1):
        first_set.add(i)
    second_set = set()
    for i in range(second_interval[0], second_interval[1] + 1):
        second_set.add(i)
    current_intersection = first_set.intersection(second_set)
    if longest_intersection:
        if len(current_intersection) > len(longest_intersection):
            longest_intersection = current_intersection
    else:
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(a) for a in longest_intersection])}] with length {len(longest_intersection)}")
