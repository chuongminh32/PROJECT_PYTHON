from tkinter import *  # Nhập tất cả các lớp và hàm từ thư viện Tkinter
from tkinter import messagebox  # Nhập thư viện messagebox để hiển thị thông báo
from PIL import Image, ImageTk  # Nhập thư viện PIL để xử lý hình ảnh
import os  # Thư viện để thao tác với các đường dẫn và tệp tin hệ thống
import subprocess  # Thư viện để gọi các chương trình ngoài ứng dụng

# Nhập các trang khác của ứng dụng
from manage_page import StudentManagementApp  # Trang quản lý sinh viên
from view_page import ViewPage  # Trang xem thông tin sinh viên

class Main:
    def __init__(self, root):
        self.root = root  # Tham chiếu đến cửa sổ chính của ứng dụng
        self.setup_window()  # Thiết lập cửa sổ
        self.create_logo()  # Tạo logo cho ứng dụng
        self.create_menu()  # Tạo menu cho ứng dụng

    def setup_window(self):
        """Thiết lập cửa sổ chính của ứng dụng."""
        self.root.title("Hệ thống quản lý sinh viên")  # Tiêu đề cửa sổ
        self.root.geometry("1000x550+300+200")  # Kích thước cửa sổ và vị trí
        self.root.configure(background="white")  # Màu nền của cửa sổ
        self.root.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ

    def create_logo(self):
        """Tạo logo cho ứng dụng."""
        logo_path = os.path.join("images", "logo_fit.png")  # Đường dẫn tới logo
        logo_image = Image.open(logo_path).resize((50, 50), Image.LANCZOS)  # Mở và thay đổi kích thước ảnh logo
        self.logo_dash = ImageTk.PhotoImage(logo_image)  # Chuyển đổi ảnh thành dạng có thể hiển thị trên Tkinter

        # Đặt logo và tên ứng dụng lên trên cùng của cửa sổ
        Label(self.root, text="Trang chủ", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        """Tạo menu cho ứng dụng."""
        M_Frame = LabelFrame(self.root, text="Menu",  # Tạo một khung LabelFrame chứa menu
                             bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)  # Đặt vị trí của khung menu

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Quản lí", self.manage, 0)
        self.create_menu_button(M_Frame, "Trực quan", self.show_view, 75)
        self.create_menu_button(M_Frame, "Sinh viên", self.stu, 150)
        self.create_menu_button(M_Frame, "Đăng xuất", self.logout, 220)
        self.create_menu_button(M_Frame, "Thoát", self.exit_program, 290)

        # Đặt nền cho phần chính của cửa sổ
        self.bg_Home = ImageTk.PhotoImage(Image.open(
            "images/bg_home.png").resize((800, 470), Image.LANCZOS))  # Mở và thay đổi kích thước ảnh nền
        Label(self.root, image=self.bg_Home).place(
            x=200, y=80, width=800, height=470)  # Đặt nền hình ảnh phía sau các nút menu

    def create_menu_button(self, parent, text, command, y_position):
        """Tạo nút menu trong khung menu."""
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"),
                        command=command)  # Tạo một nút mới
        button.place(x=0, y=y_position, width=200, height=50)  # Đặt vị trí của nút
        # Thêm hiệu ứng khi di chuột qua và ra khỏi nút
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))

    def manage(self):
        """Mở trang quản lý trong cửa sổ mới."""
        self.root.destroy()  # Đóng cửa sổ hiện tại
        subprocess.run(["python", "gui/manage_page.py"])  # Chạy trang quản lý sinh viên

    def show_view(self):
        """Chức năng xem thông tin sinh viên."""
        self.root.destroy()  # Đóng cửa sổ hiện tại
        subprocess.run(["python", "gui/view_page.py"])  # Mở trang xem thông tin sinh viên

    def logout(self):
        """Chức năng đăng xuất."""
        # Hiển thị hộp thoại xác nhận đăng xuất
        if messagebox.askyesno("Logout", "Bạn có chắc chắn muốn đăng xuất?"):
            self.root.destroy()  # Đóng cửa sổ hiện tại
            subprocess.run(["python", "gui/login_page.py"])  # Mở trang đăng nhập

    def stu(self):
        """Chức năng quản lý sinh viên."""
        self.root.destroy()  # Đóng cửa sổ hiện tại
        subprocess.run(["python", "gui/student_page.py"])  # Mở trang quản lý sinh viên

    def exit_program(self):
        """Chức năng thoát chương trình."""
        # Hiển thị hộp thoại xác nhận thoát chương trình
        if messagebox.askyesno("Exit", "Bạn có chắc chắn muốn thoát chương trình?"):
            self.root.quit()  # Thoát chương trình

if __name__ == "__main__":
    root = Tk()  # Khởi tạo cửa sổ chính Tkinter
    app = Main(root)  # Khởi tạo đối tượng Main để chạy ứng dụng
    root.mainloop()  # Vòng lặp chính của Tkinter, giúp cửa sổ luôn mở cho người dùng tương tác
