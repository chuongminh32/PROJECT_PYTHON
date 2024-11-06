from tkinter import *  # Nhập tất cả các lớp và hàm từ thư viện Tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
from manage_page import open_manage_page
from view_page import open_view_page


class Main:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()

    def setup_window(self):
        """Thiết lập cửa sổ chính."""
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")

    def create_logo(self):
        """Tạo logo cho ứng dụng."""
        logo_path = os.path.join("images", "logo.png")
        logo_image = Image.open(logo_path).resize((20, 20))
        self.logo_dash = ImageTk.PhotoImage(logo_image)

        Label(self.root, text="Student Management Mini", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        """Tạo menu cho ứng dụng."""
        M_Frame = LabelFrame(self.root, text="Menu",
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Manage", self.manage, 0)
        self.create_menu_button(M_Frame, "View", self.show_view, 75)
        self.create_menu_button(M_Frame, "Logout", self.logout, 150)
        self.create_menu_button(M_Frame, "Exit", self.exit_program, 220)

        # Nền cho khung chính
        self.bg_Home = ImageTk.PhotoImage(Image.open(
            "images/bg_home.png").resize((1150, 700), Image.LANCZOS))
        Label(self.root, image=self.bg_Home).place(
            x=200, y=80, relwidth=1, relheight=1)

    def create_menu_button(self, parent, text, command, y_position):
        """Tạo nút menu."""
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
                        command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def manage(self):
        """Chức năng quản lý."""
        self.root.destroy()
        open_manage_page()

    def show_view(self):
        """Chức năng xem."""
        self.root.destroy()
        open_view_page()

    def logout(self):
        """Chức năng đăng xuất."""
        if messagebox.askyesno("Logout", "Bạn có chắc chắn muốn đăng xuất?"):
            self.root.destroy()
            subprocess.run(["python", "gui/login_page.py"])

    def exit_program(self):
        """Chức năng thoát chương trình."""
        if messagebox.askyesno("Exit", "Bạn có chắc chắn muốn thoát chương trình?"):
            self.root.quit()


if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()
