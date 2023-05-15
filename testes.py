import tkinter as tk
from tkinter import ttk

def progressbar(x, y, max, value):

    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", foreground='none', background='#A4CE48', troughcolor='#FFFFFF', bordercolor='#FFFFFF')
    style.configure("CustomLabel.TLabel", foreground='black', background='#FFFFFF')


    progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", style="green.Horizontal.TProgressbar")
    progressbar.place(x=x,y=y)

    label = ttk.Label(root, text="", style="CustomLabel.TLabel")
    label.place(x=x+2, y=y+2)

    progressbar["maximum"] = max
    progressbar["value"] = value
    label["text"] = str(progressbar["value"]), "GB"

root = tk.Tk()
root.geometry("300x300")

progressbar(10, 0, 30, 5)
progressbar(10, 40, 30, 25)
progressbar(10, 80, 30, 15)

root.mainloop()
