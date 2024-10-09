import os

ABSTRACT_PATH = os.path.abspath("")

text_path = os.path.join(ABSTRACT_PATH, "02_Line_Numbers_Files", "text.txt")
out_path = os.path.join(ABSTRACT_PATH, "02_Line_Numbers_Files", "output.txt")
result = ""
with open(text_path) as file:
    line_number = 1
    while True:
        line = file.readline()[:-1]
        if line == "":
            break
        letter_count = 0
        marks_count = 0
        for c in line:
            if c.isalpha() or c.isnumeric():
                letter_count += 1
            elif c != " ":
                marks_count += 1
        result += f"Line {line_number} {line} ({letter_count})({marks_count})\n"
        line_number += 1

with open(out_path, "w") as file:
    file.write(result)
