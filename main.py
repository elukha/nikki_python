import tkinter as tk
from login import login
from tkinter import messagebox

root = tk.Tk()
root.title("ログインする")
width = 500
height = 400
root.geometry(f"{width}x{height}")

#IDとパスワードを入力
id_label = tk.Label(root, text="ID")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

password_label = tk.Label(root ,text="password")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

#ログインボタン
but = tk.Button(text="ログイン", background="#00ff2f", command=login)
but.pack()

login(id_entry, password_entry)

root.mainloop()
