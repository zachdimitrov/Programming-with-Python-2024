country_list = input().split(", ")
capital_list = input().split(", ")
final_capitals = {country_list[i]: capital_list[i] for i in range(len(country_list))}
#data = []
#for i in range(len(country_list)):
#    data.append((country_list[i], capital_list[i]))
#
#capitals = {country: capital for country, capital in data}

for key, value in final_capitals.items():
    print(f"{key} -> {value}")

# print(dict(zip(country_list, capital_list)))
