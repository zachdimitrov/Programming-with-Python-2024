import tkinter as tk
from canvas import app


def clear_screen():
    print(app.grid)
    for el in app.grid_slaves():
        el.destroy()

    tk.Button(app, text="Exit", command=app.destroy).grid(row=100, column=100, pady=20)
