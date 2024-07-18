lines = int(input())
synonims = {}
for i in range(lines):
    word = input()
    syn = input()
    if word not in synonims:
        synonims[word] = [syn]
    if syn not in synonims[word]:
        synonims[word].append(syn)

for key, value in synonims.items():
    print(f"{key} - {', '.join(value)}")
