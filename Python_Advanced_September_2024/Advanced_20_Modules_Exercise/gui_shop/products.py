import os
import json
import tkinter as tk
from helpers import clear_screen
from canvas import app
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)


def update_current_user(username, p):
    with open("db/users.txt", "r+", newline="\n") as file:
        users = [json.loads(line.strip()) for line in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(p)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(user) + "\n" for user in users])
                return


def purchase_products(p):
    with open("db/products.txt", "r+", newline="\n") as file:
        products = [json.loads(line.strip()) for line in file]
        for product in products:
            if product["id"] == p:
                if product["count"] > 0:
                    product["count"] -= 1
                    file.seek(0)
                    file.truncate()
                    file.writelines([json.dumps(product) + "\n" for product in products])
                    return


def buy_product(p):
    clear_screen()
    with open("db/current_user.txt") as file:
        username = file.read()

    if username:
        purchase_products(p)
        update_current_user(username, p)

    render_product_screen()


def render_product_screen():
    clear_screen()

    with open("db/products.txt") as file:
        products = [json.loads(p.strip()) for p in file]
        products_per_line = 6
        rows_per_product = len(products[0])
        for i, product in enumerate(products):
            row = i // products_per_line * rows_per_product
            col = i % products_per_line

            tk.Label(app, text=product["name"]).grid(row=row, column=col)

            img = Image.open(os.path.join(base_folder, "db", "images", product["img_path"])).resize((100, 100))
            photo_img = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_img)
            image_label.image = photo_img
            image_label.grid(row=row + 1, column=col)

            tk.Label(app, text=product["count"]).grid(row=row + 2, column=col)

            if product["count"] > 0:
                tk.Button(app,
                          text=f"Buy {product['id']}",
                          bg="green",
                          fg="white",
                          command=lambda p=product["id"]: buy_product(p)
                          ).grid(row=row + 3, column=col)
            else:
                tk.Label(app, text="Not available", bg="orange").grid(row=row + 3, column=col)

