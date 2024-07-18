product_line = input().split()
products = {}
for i in range(0, len(product_line), 2):
    key = product_line[i]
    value = product_line[i + 1]
    products[key] = int(value)

search_list = input().split()

for item in search_list:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

