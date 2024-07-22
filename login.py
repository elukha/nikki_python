import tkinter as tk
import sys
from tkinter import messagebox

def login():
    id = id_entry.get()
    password = password_entry.get()

    #IDとPASSWORDが一致するか確認
    if id == "user" and password == "2295":
        check(True)
    else:
        check(False)


#IDとパスワードを入力
id_label = tk.Label(text="ID").pack()
id_entry = tk.Entry().pack()
password_label = tk.Label(text="password").pack()
password_entry = tk.Entry().pack()

#ログインボタン
but = tk.Button(text="ログイン", background="#00ff2f", command=login())
but.pack()
    


def check(request):
    status = bool
    if request == True:
        status = True
    elif request == False:
        status = False
    elif request == "check":
        return status