import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

color_choices = ["RED","YELLOW","GREEN","BLUE","PURPLE","BLACK"]
tries = 10
code_length = 4

def generate_code():
    code = []
    for index in range(code_length):
        color = random.choice(color_choices)
        code.append(color)
    return code

def guess_code():
    guess = entry.get().upper().split(" ")
    if len(guess) != code_length:
        messagebox.showerror("Error", f"You must guess {code_length} colors")
        return  None
    for color in guess:
        if color not in color_choices:
            messagebox.showerror("Error", f"Invalid color: {color}. Try again.")
            return None
    return guess



