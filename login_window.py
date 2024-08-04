import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

#成功したか確認
def fn_login(en1, en2):
    global status
    id = en1.get()
    password = en2.get()

    print("login.py")
    #IDとPASSWORDが一致するか確認
    if id == "user" and password == "2295":
        messagebox.showinfo("情報", "ログインに成功しました")
        status = True
        print(True)
        root.destroy()
    else:
        messagebox.showerror("エラー", "ログインに失敗しました")
        status = False
        print(False)

    return status


#ウィンドウを閉じる
def login_window_close():
    root.destroy()

#ログインウィンドウ作成
def fn_login_window():
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
    but = tk.Button(text="ログイン", background="#00ff2f", command = lambda:fn_login(id_entry, password_entry))
    but.pack()

    root.mainloop()