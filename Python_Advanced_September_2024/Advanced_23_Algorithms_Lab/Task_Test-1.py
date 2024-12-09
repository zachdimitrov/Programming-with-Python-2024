import os


def find_all_files(directory):
    files_list = []

    def recursive_add(dir_path):
        for item in os.listdir(dir_path):
            full_path = os.path.join(dir_path, item)
            if os.path.isdir(full_path):
                recursive_add(full_path)
            else:
                files_list.append(full_path)
    recursive_add(directory)
    return files_list


path = input()
print(find_all_files(path))