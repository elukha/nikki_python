import tkinter as tk
import os
from tkinter import messagebox
from functools import partial


#ホーム画面
def home():
    global root
    root = tk.Tk()
    root.title("ホームページ")
    width = 400
    height = 300
    root.geometry(f"{width}x{height}")
    
   #日記を作成するボタン 
    write_button = tk.Button(text="日記を作成", command=write)
    write_button.grid(row=0, column=0)

    #dataフォルダにあるファイル名をリストで取得
    files = os.listdir("./data")
    print(files)
    
    r = 1

    for i in files:
        tkbutton = tk.Button(root, text = i[:-4], width=50, command=partial(view, i))
        tkbutton.grid(row=r, column=0)
        
        delete_button = tk.Button(root, text="削除", bg="yellow", command=partial(delete, i))
        delete_button.grid(row=r, column=20)

        r += 1

    root.mainloop()


#日記の内容を表示
def view(file_name):
    print(file_name)
    view_window = tk.Tk()
    with open('./data/'+file_name) as f:
        content = f.read()

    title = tk.Label(view_window, text="題名")
    title.pack()

    title_name = tk.Label(view_window, text=file_name[:-4])
    title_name.pack()

    text = tk.Label(view_window, text="内容")
    text.pack()

    text_content = tk.Label(view_window, text=content, bg="#c0c0c0")
    text_content.pack()


#日記を削除
def delete(file_path):
    ret = messagebox.askyesno("警告", "タイトル名:" + file_path[:-4] + "を削除しますか？")
    if ret:
        os.remove("./data/"+file_path)
        root.destroy()
        home()


#日記をファイルとして保存
def create():
    title = new_title_entry.get()
    word = new_word_entry.get(0., tk.END)
    path = f"./data/{title}.txt"
    print(len(title))
    print(len(word))
    
    if len(title) == 0:
        messagebox.showerror("エラー", "タイトルを入力してください")
    elif len(word) == 1:
        messagebox.showerror("エラー", "日記の内容を入力してください")
    else:
        with open(path, mode="w") as f:
            f.write(word)
        messagebox.showinfo("成功", "書き込みに成功しました")
        input_window.destroy()
        root.destroy()
        home()


#日記入力ウィンドウ
def write():
    global input_window
    input_window = tk.Tk()
    input_window.title("日記を新規作成")
    width = 500
    height = 400
    input_window.geometry(f"{width}x{height}")

    new_title_label = tk.Label(input_window, text="日記の題名")
    new_title_label.pack()

    global new_title_entry
    new_title_entry = tk.Entry(input_window)
    new_title_entry.pack()

    new_word_label = tk.Label(input_window, text="日記の内容を入力")
    new_word_label.pack(pady=10)

    global new_word_entry
    new_word_entry = tk.Text(input_window, bg="#c1e4e9", height=16)
    new_word_entry.pack()

    create_button = tk.Button(input_window, text="作成", command=create)
    create_button.pack()
