morse = {".-": "A",
         "-...": "B",
         "-.-.": "C",
         "-..": "D",
         ".": "E",
         "..-.": "F",
         "--.": "G",
         "....": "H",
         "..": "I",
         ".---": "J",
         "-.-": "K",
         ".-..": "L",
         "--": "M",
         "-.": "N",
         "---": "O",
         ".--.": "P",
         "--.-": "Q",
         ".-.": "R",
         "...": "S",
         "-": "T",
         "..-": "U",
         "...-": "V",
         ".--": "W",
         "-..-": "X",
         "-.--": "Y",
         "--..": "Z"}

line = list(map(lambda x: x.strip(), input().split("|")))
result = ""

for word in line:
    letters = word.split()
    for letter in letters:
        result = result + morse[letter]
    result = result + " "

print(result.strip())
