# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Frame, Entry, Button, END, messagebox, PhotoImage
import subprocess
import os
import ast
from PIL import Image, ImageTk

"""Tk: class để tạo cửa sổ chính
Label: class để thêm text hoặc hình ảnh
Frame: class để tạo container
Entry: class để tạo ô nhập liệu
Button: class để tạo nút
END: biến để xác định cuối của Entry
messagebox: class để hiển thị thông báo
os: module để thao tác với hệ thống
subprocess: module để chạy các lệnh hệ thống
Image, ImageTk: class để thao tác với hình ảnh
PhotoImage: class để thêm hình ảnh vào Label"""


def initialize_root():
    root = Tk()
    root.title("Mini Edu - Sign Up")
    root.geometry("1000x550+300+200")
    root.config(bg="white")
    root.resizable(False, False)
    return root


def add_background(root):
    img = PhotoImage(file="images/sign_up3.png")
    Label(root, image=img, bg="white", border=0).place(
        x=50, y=50, width=450, height=450)
    root.bg_image = img  # giữ tham chiếu để tránh bị xóa khỏi bộ nhớ


def create_signup_frame(root):
    frame = Frame(root, width=350, height=400, bg="white")
    frame.place(x=550, y=70)
    return frame


def add_logo_and_heading(frame):
    logo_path = os.path.join("images", "logo_fit.png")
    logo_image = ImageTk.PhotoImage(Image.open(logo_path).resize((50, 50)))
    Label(frame, image=logo_image, bg="white").place(x=20, y=10)
    frame.logo_image = logo_image
    Label(frame, text="Đăng Kí", font=("Arial", 20, "bold"),
          bg="white", fg="#1C2442").place(x=80, y=15)

# hàm add_entry() nhận thêm tham số show để ẩn mật khẩu


def add_entry(frame, placeholder, y, show=""):
    entry = Entry(frame, width=35, fg='#1C2442', border=0,
                  bg="white", font=("Arial", 11), show=show)
    entry.place(x=30, y=y)
    entry.insert(0, placeholder)
    Frame(frame, width=262, height=2, bg="#1C2442").place(x=30, y=y+25)

    def on_enter(event):
        if entry.get() == placeholder:
            entry.delete(0, END)  # Xóa placeholder

    def on_leave(event):
        if entry.get() == '':
            entry.insert(0, placeholder)  # Thêm placeholder

    entry.bind("<FocusIn>", on_enter)
    entry.bind("<FocusOut>", on_leave)
    return entry

# hàm add_signup_button() nhận thêm tham số username, password, confirm_password để kiểm tra thông tin nhập vào


def add_signup_button(frame, username, password, confirm_password):
    def signup():
        user = username.get()  # Lấy tên người dùng từ ô nhập liệu
        pwd = password.get()  # Lấy mật khẩu từ ô nhập liệu
        confirm_pwd = confirm_password.get()  # Lấy mật khẩu xác nhận từ ô nhập liệu

        if user == "Username" or pwd == "Password" or confirm_pwd == "Confirm Password":  # Kiểm tra nếu có ô nhập liệu rỗng
            # Hiển thị thông báo lỗi
            messagebox.showerror("Sign Up", "Vui lòng điền đầy đủ thông tin.")
            return

        try:
            # Mở (hoặc tạo) file users.txt trong chế độ append
            with open("data/users.txt", "a+") as file:
                file.seek(0)  # Đưa con trỏ về đầu file
                data = file.read() or "{}"  # Đọc dữ liệu từ file, nếu rỗng thì gán là dict rỗng
                users = ast.literal_eval(data)  # Chuyển đổi chuỗi thành dict

                if user in users:  # Kiểm tra nếu tên người dùng đã tồn tại
                    # Hiển thị thông báo lỗi
                    messagebox.showerror(
                        "Sign Up", "Tên người dùng đã tồn tại. Vui lòng chọn tên khác.")
                    return

                if pwd == confirm_pwd:  # Kiểm tra nếu mật khẩu và mật khẩu xác nhận khớp
                    users[user] = pwd  # Thêm người dùng mới vào dict
                    file.seek(0)
                    file.truncate()  # Xóa nội dung file trước khi ghi mới
                    file.write(str(users))  # Ghi dict người dùng vào file

                    # Hiển thị thông báo thành công
                    messagebox.showinfo(
                        "Sign Up", "Đăng ký thành công! Chuyển đến trang đăng nhập.")
                else:
                    # Hiển thị thông báo lỗi nếu mật khẩu không khớp
                    messagebox.showerror(
                        "Sign Up", "Mật khẩu không khớp. Vui lòng thử lại.")
        except Exception as e:
            # Hiển thị thông báo lỗi nếu có ngoại lệ
            messagebox.showerror("Sign Up", f"Có lỗi xảy ra: {str(e)}")

    btn_signup = Button(frame, width=26, height=2, border=0, text="Sign Up", bg="#1C2442", fg="white",
                        font=("Arial", 13, "bold"), command=signup)
    btn_signup.place(x=30, y=275)
    btn_signup.bind("<Enter>", lambda e: btn_signup.config(
        bg="grey", fg="#1C2442", cursor="hand2"))
    btn_signup.bind("<Leave>", lambda e: btn_signup.config(
        bg="#1C2442", fg="white", cursor=""))

    label = Label(frame, text="Bạn đã có tài khoản ?", font=(
        "Arial", 10), bg="white", fg="#1C2442")
    label.place(x=30, y=330)

    signin = Button(frame, width=8, text="Đăng nhập", bg="white", fg="#1C2442", font=(
        "Arial", 10, "bold"), border=0, cursor="hand2", command=lambda: go_to_login())
    signin.place(x=170, y=330)

    def go_to_login():
        root.destroy()
        subprocess.run(["python", "gui/login_page.py"])


if __name__ == "__main__":
    root = initialize_root()
    add_background(root)
    signup_frame = create_signup_frame(root)
    add_logo_and_heading(signup_frame)
    username_entry = add_entry(signup_frame, "Username", 80)
    password_entry = add_entry(signup_frame, "Password", 150)
    confirm_password_entry = add_entry(signup_frame, "Confirm Password", 220)
    add_signup_button(signup_frame, username_entry,
                      password_entry, confirm_password_entry)
    root.mainloop()
