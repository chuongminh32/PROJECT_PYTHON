from tkinter import *
from tkinter import messagebox
import subprocess
import os
from PIL import Image, ImageTk
import ast

"""
Mô tả:
    Đây là một trang đăng nhập được xây dựng bằng thư viện Tkinter trong Python. 
    Trang đăng nhập này cho phép người dùng nhập tên người dùng và mật khẩu để đăng nhập vào hệ thống.
Thư viện sử dụng:
    - tkinter: Thư viện GUI tiêu chuẩn của Python.
    - tkinter.messagebox: Thư viện con của tkinter để hiển thị các hộp thoại thông báo.
    - subprocess: Thư viện để chạy các tiến trình con.
    - os: Thư viện cung cấp nhiều chức năng liên quan đến hệ điều hành.
    - PIL (Pillow): Thư viện xử lý hình ảnh.
    - ast: Thư viện để xử lý các biểu thức Python dưới dạng chuỗi.
Lớp:
    - LoginPage: Lớp đại diện cho trang đăng nhập.
Phương thức của lớp LoginPage:
    - __init__(self, root): Khởi tạo đối tượng LoginPage.
    - add_background(self): Thêm hình nền cho trang đăng nhập.
    - create_signup_frame(self): Tạo khung cho phần đăng nhập.
    - add_logo(self): Thêm logo vào khung đăng nhập.
    - add_heading(self): Thêm tiêu đề cho khung đăng nhập.
    - add_entry(self, placeholder, y, show=""): Thêm các trường nhập liệu cho tên người dùng và mật khẩu.
    - on_enter(self, entry, placeholder, show): Xử lý sự kiện khi người dùng nhấp vào trường nhập liệu.
    - on_leave(self, entry, placeholder, show): Xử lý sự kiện khi người dùng rời khỏi trường nhập liệu.
    - add_signup_button(self): Thêm nút đăng nhập và xử lý sự kiện khi nhấp vào nút.
    - add_create_account_label(self): Thêm nhãn và nút để chuyển đến trang đăng ký tài khoản.
Hàm:
    - main(): Hàm chính để khởi chạy ứng dụng.
"""

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Edu - Sign In")  # Đặt tiêu đề cửa sổ chính
        self.root.geometry("1000x550+300+200")  # Đặt kích thước và vị trí cửa sổ
        self.root.config(bg="white")  # Đặt màu nền cho cửa sổ
        self.root.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ
        self.add_background()  # Thêm hình nền cho trang đăng nhập
        self.frame = self.create_signup_frame()  # Tạo khung đăng nhập
        self.add_logo()  # Thêm logo vào khung đăng nhập
        self.add_heading()  # Thêm tiêu đề vào khung đăng nhập
        self.username = self.add_entry("Username", 100)  # Thêm trường nhập liệu cho tên người dùng
        self.password = self.add_entry("Password", 150)  # Thêm trường nhập liệu cho mật khẩu
        self.add_signup_button()  # Thêm nút đăng nhập
        self.add_create_account_label()  # Thêm nhãn và nút để chuyển đến trang đăng ký tài khoản

    def add_background(self):
        """Thêm hình nền cho trang đăng nhập."""
        img = PhotoImage(file="images/sign_in.png")  # Đọc ảnh nền
        Label(self.root, image=img, bg="white").place(x=50, y=50)  # Đặt ảnh nền lên cửa sổ
        self.root.bg_image = img  # Lưu lại hình ảnh để không bị mất khi cửa sổ thay đổi

    def create_signup_frame(self):
        """Tạo khung đăng nhập."""
        frame = Frame(self.root, width=350, height=400, bg="white")  # Khung đăng nhập có kích thước cố định
        frame.place(x=550, y=70)  # Đặt vị trí của khung
        return frame  # Trả về khung đăng nhập

    def add_logo(self):
        """Thêm logo vào khung đăng nhập."""
        logo_image = ImageTk.PhotoImage(Image.open(
            "images/logo_fit.png").resize((50, 50)))  # Đọc logo và thay đổi kích thước
        Label(self.frame, image=logo_image, bg="white").place(x=20, y=10)  # Đặt logo vào khung đăng nhập
        self.frame.logo_image = logo_image  # Lưu hình ảnh logo để không bị mất khi cửa sổ thay đổi

    def add_heading(self):
        """Thêm tiêu đề vào khung đăng nhập."""
        Label(self.frame, text="Đăng Nhập", font=("Arial", 20, "bold"),
              bg="white", fg="#1C2442").place(x=80, y=15)  # Tiêu đề "Đăng Nhập"

    def add_entry(self, placeholder, y, show=""):
        """Thêm trường nhập liệu cho tên người dùng và mật khẩu."""
        entry = Entry(self.frame, width=25, fg='#1C2442', border=0,
                      bg="white", font=("Arial", 11), show=show)  # Tạo trường nhập liệu
        entry.place(x=30, y=y)  # Đặt trường nhập liệu vào vị trí trên khung
        entry.insert(0, placeholder)  # Thêm placeholder vào trường nhập liệu
        Frame(self.frame, width=262, height=2,
              bg="#1C2442").place(x=30, y=y+25)  # Đặt đường viền cho trường nhập liệu

        entry.bind("<FocusIn>", lambda e: self.on_enter(
            entry, placeholder, show))  # Xử lý sự kiện khi người dùng nhấp vào trường nhập liệu
        entry.bind("<FocusOut>", lambda e: self.on_leave(
            entry, placeholder, show))  # Xử lý sự kiện khi người dùng rời khỏi trường nhập liệu
        return entry  # Trả về trường nhập liệu

    def on_enter(self, entry, placeholder, show):
        """Xử lý khi người dùng nhấp vào trường nhập liệu."""
        if entry.get() == placeholder:  # Kiểm tra nếu giá trị trong trường nhập liệu là placeholder
            entry.delete(0, END)  # Xóa placeholder khi người dùng nhấp vào

    def on_leave(self, entry, placeholder, show):
        """Xử lý khi người dùng rời khỏi trường nhập liệu."""
        if entry.get() == '':  # Nếu trường nhập liệu trống
            entry.insert(0, placeholder)  # Đặt lại placeholder vào trường nhập liệu

    def add_signup_button(self):
        """Thêm nút đăng nhập và xử lý sự kiện khi người dùng nhấn nút."""
        def signin():
            u, p = self.username.get(), self.password.get()  # Lấy tên người dùng và mật khẩu
            if u != 'Username' and p != 'Password':  # Kiểm tra nếu tên người dùng và mật khẩu không phải placeholder
                try:
                    with open("data/users.txt", "r") as f:
                        users = ast.literal_eval(f.read())  # Đọc dữ liệu người dùng từ tệp
                    if u in users and users[u] == p:  # Kiểm tra nếu tên người dùng và mật khẩu hợp lệ
                        if u == "admin" and p == "111":  # Kiểm tra nếu là admin
                            messagebox.showinfo("Login", "Hi Admin !")  # Thông báo với admin
                            self.root.destroy()  # Đóng cửa sổ đăng nhập
                            subprocess.run(["python", "gui/home_page.py"])  # Mở trang chủ
                        else:
                            messagebox.showinfo(
                                "Login", "Đăng nhập thành công")  # Thông báo đăng nhập thành công
                            self.root.destroy()  # Đóng cửa sổ đăng nhập
                            subprocess.run(["python", "gui/home_page.py"])  # Mở trang chủ
                    else:
                        messagebox.showerror(
                            "Login", "Tên người dùng hoặc mật khẩu không đúng")  # Thông báo nếu đăng nhập sai
                except Exception as e:
                    messagebox.showerror(
                        "Error", f"Có lỗi xảy ra khi đọc file: {str(e)}")  # Thông báo lỗi khi đọc tệp
            else:
                messagebox.showerror(
                    "Login", "Vui lòng nhập tên người dùng và mật khẩu hợp lệ")  # Thông báo nếu thiếu thông tin

        btn_signup = Button(self.frame, width=26, height=2, border=0, text="Sign In", bg="#1C2442", fg="white",
                            font=("Arial", 13, "bold"), command=signin)  # Tạo nút đăng nhập
        btn_signup.place(x=30, y=220)  # Đặt nút vào khung
        btn_signup.bind("<Enter>", lambda e: btn_signup.config(
            bg="grey", fg="#1C2442", cursor="hand2"))  # Thay đổi màu khi di chuột vào nút
        btn_signup.bind("<Leave>", lambda e: btn_signup.config(
            bg="#1C2442", fg="white"))  # Thay đổi màu khi di chuột ra khỏi nút

    def add_create_account_label(self):
        """Thêm nhãn và nút để chuyển đến trang đăng ký tài khoản."""
        def open_signin_page():
            self.root.destroy()  # Đóng cửa sổ đăng nhập hiện tại
            subprocess.run(["python", "gui/signup_page.py"])  # Mở trang đăng ký tài khoản

        create_account_label = Label(self.frame, text="Bạn chưa có tài khoản ?", font=("Arial", 10), bg="white", fg="#1C2442")
        create_account_label.place(x=30, y=277)  # Đặt nhãn "Bạn chưa có tài khoản ?"
        
        signin = Button(self.frame, width=8, text="Đăng kí", bg="white", fg="#1C2442", font=("Arial", 10, "bold"), 
                        border=0, cursor="hand2", command=open_signin_page)  # Nút chuyển đến trang đăng ký
        signin.place(x=180, y=275)  # Đặt nút "Đăng kí" vào khung

def main():
    root = Tk()  # Khởi tạo cửa sổ chính
    LoginPage(root)  # Khởi tạo và hiển thị trang đăng nhập
    root.mainloop()  # Chạy vòng lặp chính của Tkinter

if __name__ == "__main__":
    main()  # Gọi hàm main để bắt đầu ứng dụng
