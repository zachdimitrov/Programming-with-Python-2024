import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}


    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        