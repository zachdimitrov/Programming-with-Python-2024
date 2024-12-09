import os

ABSTRACT_PATH = os.path.abspath("")
symbols = ["-", ",", ".", "!", "?"]
text_path = os.path.join(ABSTRACT_PATH, "01_Even_Lines_Files", "text.txt")
line_number = 0
with open(text_path) as file:
    while True:
        line = file.readline()
        if line == "":
            break
        if line_number % 2 == 0:
            for sym in symbols:
                if sym in line:
                    line = line.replace(sym, "@")
            words = line[:-1].split()
            print(" ".join(words[::-1]))
        line_number += 1
