import os

ABSTRACT_PATH = os.path.abspath("")
dir_path = os.path.join(ABSTRACT_PATH, "04_Directory_Traversal_Files")

files = {}


def get_files(folder, level):
    if level < 0 and level != -2:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = os.path.splitext(element)[1] # element.split(".")[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(f, level - 1 if level != -2 else level)


get_files(dir_path, 2)
print(files)


