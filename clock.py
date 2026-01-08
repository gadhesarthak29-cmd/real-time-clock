import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)  # update every second

root = tk.Tk()
root.title("Real-Time Clock")

label = tk.Label(root, font=("algebraic", 48), fg="black")
label.pack()

update_clock()
root.mainloop()