from tkinter import *
from tkinter import messagebox  # Nhập khẩu messagebox
from PIL import Image, ImageTk
import os
import subprocess  # Nhập khẩu subprocess

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
        
        # Đặt kích thước cửa sổ
        self.root.geometry("1350x700")
        
        # Đặt màu nền cho cửa sổ
        self.root.configure(background="white")

        # === ICON === 
        logo_path = os.path.join("images", "logo2.png")
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"File not found: {logo_path}")
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((40, 40), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo_image)

        # === TITLE ===
        title = Label(self.root, text="Student Management System", image=self.logo_dash, padx=10, compound=LEFT, bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
        title.place(x=0, y=0, relwidth=1, height=80)  # Đặt chiều cao là 80 để phù hợp với kích thước logo

        # === MENU === 
        M_Frame = LabelFrame(self.root, text="Menu", bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)  # Điều chỉnh vị trí y của menu

        # Thêm các nút vào khung menu và thiết lập hiệu ứng khi di chuột vào
        self.create_menu_button(M_Frame, "Courses", self.show_courses, 0)
        self.create_menu_button(M_Frame, "Student", self.show_students, 75)
        self.create_menu_button(M_Frame, "Result", self.show_results, 150)
        self.create_menu_button(M_Frame, "View", self.show_view, 220)
        self.create_menu_button(M_Frame, "Logout", self.logout, 290)
        self.create_menu_button(M_Frame, "Exit", self.exit_program, 360)

        # === MAIN FRAME ===
        self.bg_Home = Image.open("images/bg_home_2.jpg")
        self.bg_Home = self.bg_Home.resize((1150, 700), Image.LANCZOS)
        self.bg_Home = ImageTk.PhotoImage(self.bg_Home)
        Label(self.root, image=self.bg_Home).place(x=200, y=80, relwidth=1, relheight=1)  # Điều chỉnh vị trí y của hình nền

    def create_menu_button(self, parent, text, command, y_position):
        """Tạo một nút trong menu với hiệu ứng khi di chuột vào"""
        button = Button(parent, text=text, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
        button.place(x=0, y=y_position, width=200, height=50)
        
        # Thêm hiệu ứng cho nút
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))
        
        return button

    def show_courses(self):
        messagebox.showinfo("Courses", "Hiển thị danh sách khóa học.")

    def show_students(self):
        messagebox.showinfo("Students", "Hiển thị danh sách sinh viên.")

    def show_results(self):
        messagebox.showinfo("Results", "Hiển thị kết quả.")

    def show_view(self):
        messagebox.showinfo("View", "Hiển thị thông tin.")

    def logout(self):
        if messagebox.askyesno("Logout", "Bạn có chắc chắn muốn đăng xuất?"):
            self.root.destroy()  # Đóng cửa sổ hiện tại trước khi mở trang đăng nhập
            subprocess.run(["python", "gui/login_page.py"])  # Mở file login_page.py

    def exit_program(self):
        self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = RMS(root)
    root.mainloop()
