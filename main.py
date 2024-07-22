import tkinter as tk
import login

#ウィンドウの作成と、Tkinterオブジェクトの取得
root = tk.Tk()

#タイトル
root.title("日記")

#ウィンドウサイズ
width = 500
height = 400
root.geometry(f"{width}x{height}")
if login.input():
    print("pass")
    
root.mainloop()


login.input()

status = login.check("check")
if status:
    print("成功")
else:
    print("失敗")

