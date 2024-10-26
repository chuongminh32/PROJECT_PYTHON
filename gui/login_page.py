from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập hệ thống quản lý sinh viên")
        self.root.geometry("1350x700")
        self.root.configure(bg="#1C2442")

        # === Ảnh nền và logo ===
        bg_image = ImageTk.PhotoImage(Image.open("images/bg_login.png").resize((675, 700), Image.LANCZOS))
        logo_image = ImageTk.PhotoImage(Image.open("images/logo2.png").resize((40, 40), Image.LANCZOS))

        Label(root, image=bg_image).place(relwidth=0.5, relheight=1)  # Ảnh nền
        self.login_frame = Frame(root, bg="white")
        self.login_frame.place(relx=0.5, relheight=1, relwidth=0.5)

        Label(self.login_frame, image=logo_image, bg="white").grid(row=0, column=0, columnspan=2, pady=20)
        Label(self.login_frame, text="Login", bg="white", fg="#1C2442", font=("Arial", 24, "bold")).grid(row=1, column=0, columnspan=2, pady=10)

        # === Form đăng nhập ===
        Label(self.login_frame, text="Username:", bg="white", fg="#1C2442", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.username_entry = Entry(self.login_frame, font=("Arial", 12), width=30)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10)

        Label(self.login_frame, text="Password:", bg="white", fg="#1C2442", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.password_entry = Entry(self.login_frame, show="*", font=("Arial", 12), width=30)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)

        # === Nút đăng nhập ===
        btn_login = Button(self.login_frame, text="Log In", bg="#242533", fg="white", font=("Arial", 12, "bold"), command=self.login)
        btn_login.grid(row=4, column=0, columnspan=2, pady=20)
        btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#3B3F4C"))
        btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#242533"))

        # Lưu ảnh để tránh bị xóa bộ nhớ
        self.bg_image = bg_image
        self.logo_image = logo_image

    def login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "1234":
            messagebox.showinfo("Login", "Đăng nhập thành công!")
            self.root.destroy()
            subprocess.run(["python", "home_page.py"])
        else:
            messagebox.showerror("Login", "Tên đăng nhập hoặc mật khẩu không hợp lệ")

if __name__ == "__main__":
    root = Tk()
    app = LoginGUI(root)
    root.mainloop()
