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

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
            color_counts[color] += 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    for guess_color, real_color in zip(guess, real_code):
        if (guess_color in color_counts and color_counts[guess_color] > 0 and guess_color != real_color):
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    return correct_pos, incorrect_pos




