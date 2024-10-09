import os
import re

from constants import ABSTRACT_PATH

words_path = os.path.join(ABSTRACT_PATH, "05_Files", "words.txt")
input_path = os.path.join(ABSTRACT_PATH, "05_Files", "input.txt")
output_path = os.path.join(ABSTRACT_PATH, "05_Files", "output.txt")

with open(words_path) as file:
    try:
        words = file.read().split()
    except FileNotFoundError:
        print("File not found")

with open(input_path) as file:
    try:
        content = file.read()
    except FileNotFoundError:
        print("File not found")

occ = {}

for word in words:
    pattern = re.compile(f"\\b{word}\\b", re.IGNORECASE)
    found = re.findall(pattern, content)
    occ[word] = len(found)

sorted_occ = sorted(occ.items(), key=lambda x: -x[1])

with open(output_path, "w") as file:
    for key, val in sorted_occ:
        file.write(f"{key} - {val}\n")
