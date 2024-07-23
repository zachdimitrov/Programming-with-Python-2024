import re
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

total = 0
all_items = []

while True:
    line = input()
    if line == "Purchase":
        break
    items = re.findall(pattern, line)
    if len(items) > 0:
        all_items.append(items[0][0])
        price = float(items[0][1])
        quantity = int(items[0][2])
        total += (price * quantity)

print("Bought furniture:")
for i in all_items:
    print(i)
print(f"Total money spend: {total:.2f}")
