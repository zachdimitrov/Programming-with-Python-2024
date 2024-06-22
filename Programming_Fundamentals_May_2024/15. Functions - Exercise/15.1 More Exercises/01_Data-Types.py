def data_manipulate(data_type, data):
    if data_type == "int":
        print(int(data) * 2)
    elif data_type == "real":
        print(f"{float(data) * 1.5:.2f}")
    elif data_type == "string":
        print(f"${data}$")


d_type = input()
d = input()

data_manipulate(d_type, d)


