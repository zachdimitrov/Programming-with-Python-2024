n, m = [int(el) for el in input().split()]

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

in_both = n_set & m_set
print(*in_both, sep="\n")
