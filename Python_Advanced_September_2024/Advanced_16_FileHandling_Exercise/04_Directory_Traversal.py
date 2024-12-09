import os

ABSTRACT_PATH = os.path.abspath("")
dir_path = os.path.join(ABSTRACT_PATH, "04_Directory_Traversal_Files")

files = {}


def add_to_dict(name):
    file_name, ext = name.split(".")
    if ext not in files:
        files[ext] = []
    files[ext].append(file_name)


for element in os.listdir(dir_path):
    f = os.path.join(dir_path, element)
    if os.path.isfile(f):
        add_to_dict(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                add_to_dict(el)

# # my solution
# for name in os.listdir(dir_path):
#     if "." not in name:
#         nested_path = os.path.join(dir_path, name)
#         for file in os.listdir(nested_path):
#             add_to_dict(file)
#     else:
#         add_to_dict(name)


sorted_files = dict(sorted(files.items(), key=lambda x: (x[0])))

for key, val in sorted_files.items():
    print(f".{key}")
    sorted_val = sorted(val)
    for elem in sorted_val:
        print(f"- - - {elem}.{key}")
