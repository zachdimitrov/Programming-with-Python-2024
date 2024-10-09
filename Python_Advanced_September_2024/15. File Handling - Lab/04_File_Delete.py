import os

from constants import ABSTRACT_PATH

path = os.path.join(ABSTRACT_PATH, "nested.txt")

try:
    if not os.path.exists(path):
        print("File not found!")
    os.remove(path)
    print("File deleted!")
except FileNotFoundError:
    print("File already deleted!")
