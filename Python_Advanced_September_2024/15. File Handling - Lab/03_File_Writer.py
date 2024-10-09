with open("nested.txt", "a") as file:
    try:
        file.write("I just created my first file!")
        file.write("\nanother line")
        file.close()
    except FileNotFoundError:
        print("Something is wrong")
