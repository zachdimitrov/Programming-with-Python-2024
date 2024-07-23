import re
text = input()
pattern = r"\s(([a-z0-9]+)[0-9a-z\.\-_]*)@([a-z\-]+)(\.[a-z]+)+"
emails = re.finditer(pattern, text)
for email in emails:
    print(email.group())
