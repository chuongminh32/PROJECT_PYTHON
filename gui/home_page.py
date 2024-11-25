from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  
import os 
import subprocess 

"""
Mô tả:
    Đây là một trang chủ được xây dựng bằng thư viện Tkinter trong Python. 
    Trang chủ này cung cấp giao diện người dùng để quản lý sinh viên với các chức năng như quản lý, trực quan, sinh viên, đăng xuất và thoát chương trình.
Thư viện sử dụng:
    - tkinter: Thư viện GUI tiêu chuẩn của Python.
    - tkinter.messagebox: Thư viện con của tkinter để hiển thị các hộp thoại thông báo.
    - subprocess: Thư viện để chạy các tiến trình con.
    - os: Thư viện cung cấp nhiều chức năng liên quan đến hệ điều hành.
    - PIL (Pillow): Thư viện xử lý hình ảnh.
Lớp:
    - HomePage: Lớp đại diện cho trang chủ.
Phương thức của lớp HomePage:
    - __init__(self, root): Khởi tạo đối tượng HomePage.
    - setup_window(self): Thiết lập cửa sổ chính của ứng dụng.
    - create_logo(self): Tạo và hiển thị logo trên trang chủ.
    - create_menu(self): Tạo và hiển thị menu với các chức năng quản lý.
    - create_menu_button(self, parent, text, command, y_position): Tạo các nút trong menu.
    - manage(self): Chuyển đến trang quản lý.
    - show_view(self): Chuyển đến trang trực quan.
    - logout(self): Xử lý đăng xuất khỏi hệ thống.
    - stu(self): Chuyển đến trang sinh viên.
    - exit_program(self): Thoát khỏi chương trình.
    - run_subprocess(self, script): Chạy một tiến trình con để mở một script khác.
"""


class HomePage:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()

    def setup_window(self):
        self.root.title("Hệ thống quản lý sinh viên")
        # width x height + X + Y (X, Y: vị trí hiển thị cửa sổ)
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")
        self.root.resizable(False, False)

    def create_logo(self):
        logo_image = Image.open(os.path.join("images", "logo_fit.png")).resize((50, 50), Image.LANCZOS) # LANCZOS: một thuật toán lọc hình ảnh
        self.logo_dash = ImageTk.PhotoImage(logo_image) # Chuyển ảnh sang định dạng hình ảnh của Tkinter
        Label(self.root, text="Trang chủ", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)
        menu_items = [("Quản lí", self.manage), ("Trực quan", self.show_view),
                      ("Thống kê", self.stu), ("Đăng xuất", self.logout), ("Thoát", self.exit_program)]
        for i, (text, command) in enumerate(menu_items):
            # i * 75: mỗi nút cách nhau 75 đơn vị y
            self.create_menu_button(M_Frame, text, command, i * 75)
        self.bg_Home = ImageTk.PhotoImage(Image.open("images/bg_home.png").resize(
            (800, 470), Image.LANCZOS))  # LANCZOS: một thuật toán lọc hình ảnh
        Label(self.root, image=self.bg_Home).place(
            x=200, y=80, width=800, height=470)  # Hiển thị hình nền

    def create_menu_button(self, parent, text, command, y_position):
        button = Button(parent, text=text, border=0, bg="#242533",
                        fg="white", font=("Arial", 12, "bold"),cursor="hand2", command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def manage(self):
        self.run_subprocess("gui/manage_page.py")

    def show_view(self):
        self.run_subprocess("gui/view_page.py")

    def logout(self):
        if messagebox.askyesno("Logout", "Bạn có chắc chắn muốn đăng xuất?"):
            self.run_subprocess("gui/login_page.py")

    def stu(self):
        self.run_subprocess("gui/student_page.py")

    def exit_program(self):
        if messagebox.askyesno("Exit", "Bạn có chắc chắn muốn thoát chương trình?"):
            self.root.quit()

    def run_subprocess(self, script):
        self.root.destroy()
        subprocess.run(["python", script])


if __name__ == "__main__":
    root = Tk()
    app = HomePage(root)
    root.mainloop()
