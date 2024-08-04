from login_window import fn_login_window
import login_window
from home_page import home
from time import sleep

#ログインウィンドウを表示
fn_login_window()

#login_window IDとパスワードが一致しているかを確認する
while True:
    if login_window.status == True:
        home()
        break
    sleep(0.1)

print()