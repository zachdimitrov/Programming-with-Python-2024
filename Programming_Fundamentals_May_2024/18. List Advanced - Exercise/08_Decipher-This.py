cipher = input().split(" ")

for i in range(0, len(cipher)):
    first_letter = ""
    word = cipher[i]
    for letter in word:
        if letter.isdigit():
            first_letter += letter
    if first_letter != "":
        new_first_letter = chr(int(first_letter))
        word = word.replace(first_letter, new_first_letter)
        if len(word) > 2:
            w = [*word]
            w[1], w[-1] = w[-1], w[1]
            word = ''.join(w)
        cipher[i] = word

print(" ".join(cipher))
