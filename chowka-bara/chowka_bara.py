import tkinter as tk
import random

root = tk.Tk()

canvas = tk.Canvas(root, width=470, height=200)
canvas.pack()

def draw_dice():
    color = 'white' if random.choice([True, False]) else 'black'
    canvas.create_rectangle(10, 10, 100, 100, fill=color)
    color = 'white' if random.choice([True, False]) else 'black'
    canvas.create_rectangle(120, 10, 220, 100, fill=color)
    color = 'white' if random.choice([True, False]) else 'black'
    canvas.create_rectangle(240, 10, 340, 100, fill=color)
    color = 'white' if random.choice([True, False]) else 'black'
    canvas.create_rectangle(360, 10, 460, 100, fill=color)

draw_dice()
play_again_button = tk.Button(root, text="Play Again", command=draw_dice)
exit_button = tk.Button(root, text="Exit", fg="red", command=quit)

play_again_button.place(x=185, y=150)
exit_button.pack(side=tk.BOTTOM)


root.mainloop()
