from math import floor, ceil
days = int(input())
food = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
tur_food_gr = float(input())

dog_food_need = days * dog_food_kg
cat_food_need = days * cat_food_kg
tur_food_need = days * tur_food_gr * 0.001

all_food_need = dog_food_need + cat_food_need + tur_food_need

if all_food_need <= food:
    print(f'{floor(food - all_food_need)} kilos of food left.')
else:
    print(f'{ceil(all_food_need - food)} more kilos of food are needed.')
