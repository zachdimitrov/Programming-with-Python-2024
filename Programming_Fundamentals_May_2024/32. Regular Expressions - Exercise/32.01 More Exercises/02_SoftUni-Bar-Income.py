import re
pattern = r"%([A-Z][a-z]+)%|<(\w+)>|\|(\d+)\||(\d+\.*\d+)\$"
command = input()
total = 0
while command != "end of shift":
    data = re.findall(pattern, command)
    products = {}
    for i in range(len(data)):
        for word in data[i]:
            if word:
                products[i] = word
    if len(products) == 4:
        count = int(products[2])
        print(f"{products[0]}: {products[1]} - {count * float(products[3]):.2f}")
        total += (count * float(products[3]))
    command = input()

print(f"Total income: {total:.2f}")