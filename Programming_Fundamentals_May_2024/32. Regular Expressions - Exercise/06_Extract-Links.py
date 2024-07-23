import re
pattern = r"(www\.([A-Za-z0-9\-]+)(\.[a-z]+)+)"

line = input()
while line:
    links = re.search(pattern, line)
    if links:
        print(links.group(1))
    line = input()
