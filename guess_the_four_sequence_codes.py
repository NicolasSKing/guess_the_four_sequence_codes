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
        if guess_color in color_counts and color_counts[guess_color] > 0 and guess_color != real_color:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    return correct_pos, incorrect_pos

root = tk.Tk()
root.title("MASTERMIND")
root.geometry("1000x600")
root.resizable(False, False)

background_image = Image.open("backgroun tkinter game.jpg")
background_image = background_image.resize((1000, 600))
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

code = generate_code()
attempt = 0

title_label = tk.Label(root, text="Mastermind", font=("Comic Sans Ms", 20, "bold"), fg="black", bg="purple")
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter 4 colors separated by space (example: RED BLUE GREEN YELLOW)", font=("Arial", 15, "bold"), fg="black", bg="purple")
instruction_label.pack()

colors_label = tk.Label(root, text="Valid colors: " + ",".join(color_choices), font=("Arial", 15, "bold"), fg="black", bg="purple")
colors_label.pack(pady=5, padx=5)

entry = tk.Entry(root, width=50, font=("Arial", 12, "bold"), fg="#000000", bg="#f0f0f0", bd=3, relief="sunken",)
entry.pack(pady=10, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 15, "bold"), fg="black", bg="green")
result_label.pack(pady=10, padx=10)

attempt_label = tk.Label(root, text=f"Attempts left: {tries}", font=("Arial", 15, "bold"), fg="black", bg="green")
attempt_label.pack()

def submit_guess():
    global attempt
    guess = guess_code()
    if guess is None:
        return
    attempt += 1
    correct_pos, incorrect_pos = check_code(guess, code)
    result_label.config(text=f"Correct Position: {correct_pos} | Wrong Positon: {incorrect_pos}")
    attempt_label.config(text=f"Attempts left: {tries - attempt}")
    entry.delete(0, tk.END)
    if correct_pos == code_length:
        messagebox.showinfo("Winner!", f"You guessed the code in {attempt} tries!.")
        root.destroy()
    elif attempt == tries:
        messagebox.showinfo("Game Over", f"You ran out of tries1\nCode was: {' '.join(code)}")
        root.destroy()

submit_button = tk.Button(root, text="Submit Guess", command=submit_guess, bg="#4CAF50", fg="white", font=("Comic Sans Ms", 14, "bold"), activebackground="#45a049", relief="raised", bd=5,)
submit_button.pack(pady=10)

root.mainloop()






