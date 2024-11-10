from tkinter import *
from tkinter import messagebox
import subprocess
import os
from PIL import Image, ImageTk
import ast


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Edu - Sign In")
        self.root.geometry("1000x550+300+200")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.add_background()
        self.frame = self.create_signup_frame()
        self.add_logo()
        self.add_heading()
        self.username = self.add_entry("Username", 100)
        self.password = self.add_entry("Password", 150)
        self.add_signup_button()
        self.add_create_account_label()

    def add_background(self):
        img = PhotoImage(file="images/sign_in.png")
        Label(self.root, image=img, bg="white").place(x=50, y=50)
        self.root.bg_image = img

    def create_signup_frame(self):
        frame = Frame(self.root, width=350, height=400, bg="white")
        frame.place(x=550, y=70)
        return frame

    def add_logo(self):
        logo_image = ImageTk.PhotoImage(Image.open(
            "images/logo_fit.png").resize((50, 50)))
        Label(self.frame, image=logo_image, bg="white").place(x=20, y=10)
        self.frame.logo_image = logo_image

    def add_heading(self):
        Label(self.frame, text="Đăng Nhập", font=("Arial", 20, "bold"),
              bg="white", fg="#1C2442").place(x=80, y=15)

    def add_entry(self, placeholder, y, show=""):
        entry = Entry(self.frame, width=25, fg='#1C2442', border=0,
                      bg="white", font=("Arial", 11), show=show)
        entry.place(x=30, y=y)
        entry.insert(0, placeholder)
        Frame(self.frame, width=262, height=2,
              bg="#1C2442").place(x=30, y=y+25)

        entry.bind("<FocusIn>", lambda e: self.on_enter(
            entry, placeholder, show))
        entry.bind("<FocusOut>", lambda e: self.on_leave(
            entry, placeholder, show))
        return entry

    def on_enter(self, entry, placeholder, show):
        if entry.get() == placeholder:
            entry.delete(0, END)

    def on_leave(self, entry, placeholder, show):
        if entry.get() == '':
            entry.insert(0, placeholder)

    def add_signup_button(self):
        def signin():
            u, p = self.username.get(), self.password.get()
            if u != 'Username' and p != 'Password':
                try:
                    with open("data/users.txt", "r") as f:
                        users = ast.literal_eval(f.read())
                    if u in users and users[u] == p:
                        if u == "chuongdepzai" and p == "23571131179123":
                            messagebox.showinfo("Login", "Hi Admin !")
                            self.root.destroy()
                            subprocess.run(["python", "gui/home_page.py"])
                        else:
                            messagebox.showinfo(
                                "Login", "Đăng nhập thành công")
                            self.root.destroy()
                            subprocess.run(["python", "gui/home_page_user.py"])
                    else:
                        messagebox.showerror(
                            "Login", "Tên người dùng hoặc mật khẩu không đúng")
                except Exception as e:
                    messagebox.showerror(
                        "Error", f"Có lỗi xảy ra khi đọc file: {str(e)}")
            else:
                messagebox.showerror(
                    "Login", "Vui lòng nhập tên người dùng và mật khẩu hợp lệ")

        btn_signup = Button(self.frame, width=26, height=2, border=0, text="Sign In", bg="#1C2442", fg="white",
                            font=("Arial", 13, "bold"), command=signin)
        btn_signup.place(x=30, y=220)
        btn_signup.bind("<Enter>", lambda e: btn_signup.config(
            bg="grey", fg="#1C2442", cursor="hand2"))
        btn_signup.bind("<Leave>", lambda e: btn_signup.config(
            bg="#1C2442", fg="white"))

    def add_create_account_label(self):
        def open_signin_page():
            self.root.destroy()
            subprocess.run(["python", "gui/signup_page.py"])

        create_account_label = Label(self.frame, text="Bạn chưa có tài khoản ?", font=(
            "Arial", 10), bg="white", fg="#1C2442")
        create_account_label.place(x=30, y=277)

        signin = Button(self.frame, width=8, text="Đăng kí", bg="white", fg="#1C2442", font=(
            "Arial", 10, "bold"), border=0, cursor="hand2", command=open_signin_page)
        signin.place(x=180, y=275)


def main():
    root = Tk()
    LoginPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
