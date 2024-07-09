words = input().split(" ")
pals = []
palindrome = input()
times_found = 0

for i in range(0, len(words)):
    is_palindrome = True
    word = words[i]
    for j in range(0, len(word)//2):
        if word[j] != word[len(word) - j - 1]:
            is_palindrome = False
    if is_palindrome:
        pals.append(word)
    if word == palindrome:
        times_found += 1

print(pals)
print(f"Found palindrome {times_found} times")
