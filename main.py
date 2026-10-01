import tkinter as tk
from datetime import datetime


def log_key(event):
    key = event.keysym

    if key == "space":
        key = " "
    elif key == "Return":
        key = "\n"
    elif len(key) > 1:
        key = f"[{key}]"

    with open("keylog.txt", "a", encoding="utf-8") as file:
        file.write(key)


def clear_text():
    text_box.delete("1.0", tk.END)


window = tk.Tk()
window.title("Keylogger - Educational Demo")
window.geometry("600x400")

title = tk.Label(
    window,
    text="Keylogger - Educational Demo",
    font=("Arial", 16)
)
title.pack(pady=10)

info = tk.Label(
    window,
    text="Type inside this window. Your keystrokes will be saved to keylog.txt.",
    font=("Arial", 10)
)
info.pack(pady=5)

text_box = tk.Text(window, height=12, width=65)
text_box.pack(pady=10)

text_box.bind("<Key>", log_key)

clear_button = tk.Button(
    window,
    text="Clear",
    command=clear_text
)
clear_button.pack()

window.mainloop()