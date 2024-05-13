veg_price = float(input())
fruit_price = float(input())
full_veg_weight = int(input())
full_fruit_weight = int(input())
euro = 1.94

print(f'{(veg_price * full_veg_weight + fruit_price * full_fruit_weight) / euro:.2f}')

