from tkinter import *
from tkinter import messagebox
import subprocess
import os
from PIL import Image, ImageTk

def initialize_root():
    root = Tk()
    root.title("Mini Edu - Login")
    root.geometry("1000x550+300+200")
    root.config(bg="white")
    root.resizable(False, False)
    return root

def add_background(root):
    img = PhotoImage(file="images/bg_login.png")
    Label(root, image=img, bg="white").place(x=50, y=50)
    root.bg_image = img  # Giữ tham chiếu để tránh bị xóa khỏi bộ nhớ

def create_login_frame(root):
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=550, y=70)
    return frame

def add_logo(frame):
    logo_path = os.path.join("images", "logo_ute.png")
    logo_image = ImageTk.PhotoImage(Image.open(logo_path).resize((50, 50)))
    Label(frame, image=logo_image, bg="white").place(x=20, y=10)
    frame.logo_image = logo_image  # Giữ tham chiếu

def add_heading(frame):
    Label(frame, text="Mini Edu System", font=("Arial", 20, "bold"), bg="white", fg="#1C2442").place(x=80, y=15)

def add_password_entry(frame):
    password = Entry(frame, width=25, fg='#1C2442', border=0, bg="white", font=("Arial", 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')
    Frame(frame, width=262, height=2, bg="#1C2442").place(x=30, y=175)

    # Sự kiện cho trường nhập mật khẩu
    def on_enter(event):
        if password.get() == 'Password':
            password.delete(0, END)
            password.config(show="*")

    def on_leave(event):
        if password.get() == '':
            password.insert(0, 'Password')
            password.config(show="")

    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)
    return password

def add_login_button(frame, password):
    def login():
        if password.get() == "123":  # Giả định mật khẩu là "123"
            messagebox.showinfo("Login", "Đăng nhập thành công!")
            root.destroy()
            subprocess.run(["python", "gui/home_page.py"])  # Chuyển đến trang mới
        else:
            messagebox.showerror("Login", "Mật khẩu không chính xác")

    btn_login = Button(frame, width=26, border=0, text="Login", bg="#1C2442", fg="white", 
                       font=("Arial", 13, "bold"), command=login)
    btn_login.place(x=30, y=220)

    # Sự kiện cho nút đăng nhập
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="grey", fg="#1C2442"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#1C2442", fg="white"))

def main():
    global root
    root = initialize_root()
    add_background(root)

    frame = create_login_frame(root)
    add_logo(frame)
    add_heading(frame)
    password = add_password_entry(frame)
    add_login_button(frame, password)

    root.mainloop()

if __name__ == "__main__":
    main()
