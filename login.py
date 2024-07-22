import tkinter as tk
import sys
from tkinter import messagebox

def login(en1 :tk.Entry, en2 :tk.Entry):
    id = en1.get()
    password = en2.get()

    #IDとPASSWORDが一致するか確認
    if id == "user" and password == "2295":
        messagebox.showinfo("")
    else:
        messagebox.showerror("")