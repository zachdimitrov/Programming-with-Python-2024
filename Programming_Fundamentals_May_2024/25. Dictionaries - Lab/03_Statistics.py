statistics = {}
command = input()
while command != "statistics":
    key_value = command.split(": ")
    key = key_value[0]
    value = int(key_value[1])
    if key not in statistics:
        statistics[key] = 0
    statistics[key] += value
    command = input()

print("Products in stock:")
for (product, quantity) in statistics.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(statistics.keys())}")
print(f"Total Quantity: {sum(statistics.values())}")

