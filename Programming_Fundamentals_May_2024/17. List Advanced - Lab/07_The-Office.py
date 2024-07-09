happiness_list = number_list = list(map(int, input().split(" ")))
happiness_factor = int(input())

happiness_list = list(map(lambda x: x * happiness_factor, happiness_list))
filtered_list = list(filter(lambda x: x >= (sum(happiness_list) / len(happiness_list)), happiness_list))

if len(filtered_list) >= len(happiness_list) / 2:
    print(f'Score: {len(filtered_list)}/{len(happiness_list)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_list)}/{len(happiness_list)}. Employees are not happy!')
