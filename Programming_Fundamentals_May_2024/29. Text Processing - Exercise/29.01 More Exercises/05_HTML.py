title = input()
content = input()
comments = []
while True:
    command = input()
    if command == "end of comments":
        break
    comments.append(command)

print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t{content}\n</article>")
for comment in comments:
    print(f"<div>\n\t{comment}\n</div>")
