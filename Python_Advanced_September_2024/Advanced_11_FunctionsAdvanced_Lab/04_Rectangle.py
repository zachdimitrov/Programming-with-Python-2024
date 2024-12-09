def rectangle(length: int, width: int):
    if isinstance(length, int) and isinstance(width, int):
        return f"Rectangle area: {length * width}\n" \
            f"Rectangle perimeter: {2*(length + width)}"
    else:
        return "Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))



