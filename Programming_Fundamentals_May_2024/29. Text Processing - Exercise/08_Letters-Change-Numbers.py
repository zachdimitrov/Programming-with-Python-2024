texts = input().split()
final_sum = 0
for text in texts:
    if not text or len(text) <= 2:
        continue

    result = int(text[1:-1])
    first_letter = text[0]
    last_letter = text[len(text) - 1]
    if first_letter == first_letter.lower():
        first_position = ord(first_letter) - 96
        result = result * first_position
    else:
        first_position = ord(first_letter) - 64
        result = result / first_position
    if last_letter == last_letter.lower():
        last_position = ord(last_letter) - 96
        result = result + last_position
    else:
        last_position = ord(last_letter) - 64
        result = result - last_position

    final_sum += result

print(f"{final_sum:.2f}")

