import re

line = input()
pattern = r"(#[A-Za-z]{3,}##[A-Za-z]{3,}#)|(@[A-Za-z]{3,}@@[A-Za-z]{3,}@)"
pairs = re.findall(pattern, line)
mirrors = []
number_pairs = 0
for group in pairs:
    for pair in group:
        if pair:
            number_pairs += 1
            result = re.split("[#]+|[@]+", pair)
            if result[1] == result[2][::-1]:
                mirrors.append((result[1], result[2]))

if number_pairs > 0:
    print(f"{number_pairs} word pairs found!")
else:
    print("No word pairs found!")

if mirrors:
    print("The mirror words are:")
    for i in range(len(mirrors)):
        print(f"{mirrors[i][0]} <=> {mirrors[i][1]}", end="")
        if mirrors[i] != mirrors[len(mirrors) - 1]:
            print(", ", end="")
else:
    print("No mirror words!")

#@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r