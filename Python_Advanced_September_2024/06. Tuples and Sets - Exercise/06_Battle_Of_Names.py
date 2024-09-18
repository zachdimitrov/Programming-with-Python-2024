n = int(input())
names_even = set()
names_odd = set()
for i in range(n):
    current = input()
    value = 0
    for c in current:
        value += ord(c)
    divided_value = value//(i + 1)
    if divided_value % 2 == 0:
        names_even.add(divided_value)
    else:
        names_odd.add(divided_value)

odd_sum = sum(names_odd)
even_sum = sum(names_even)
result = set()
if odd_sum == even_sum:
    result = names_odd.union(names_even)
elif odd_sum > even_sum:
    result = names_odd.difference(names_even)
elif even_sum > odd_sum:
    result = names_odd.symmetric_difference(names_even)

print(f"{', '.join(str(a) for a in result)}")
