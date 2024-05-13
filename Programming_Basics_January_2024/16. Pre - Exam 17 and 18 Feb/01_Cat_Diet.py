fat = int(input())
protein = int(input())
carbs = int(input())
calories = int(input())
water = int(input())

grams_fat = (fat * calories / 100) / 9
grams_protein = (protein * calories / 100) / 4
grams_carbs = (carbs * calories / 100) / 4

all_food = grams_protein + grams_fat + grams_carbs

calories_per_gram = calories / all_food

print(f'{(100 - water) * calories_per_gram / 100:.4f}')
