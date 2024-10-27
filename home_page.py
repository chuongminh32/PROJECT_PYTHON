from tkinter import *  # Nhập tất cả các lớp và hàm từ thư viện Tkinter
from tkinter import messagebox  # Nhập messagebox để hiển thị thông báo cho người dùng
from PIL import Image, ImageTk  # Nhập các lớp để làm việc với hình ảnh từ thư viện PIL (Pillow)
import os  # Nhập thư viện để làm việc với hệ thống tệp
import subprocess  # Nhập thư viện để thực thi các lệnh hệ thống
from gui.manage_page import open_manage_page  # Nhập hàm mở trang quản lý từ file manage_page.py


class Main:
    def __init__(self, root):
        """Khởi tạo ứng dụng chính với cửa sổ root."""
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")  # Đặt tiêu đề cho cửa sổ
        self.root.geometry("1350x700")  # Đặt kích thước cửa sổ
        self.root.configure(background="white")  # Đặt màu nền cho cửa sổ

        # === ICON === 
        logo_path = os.path.join("images", "logo2.png")  # Đường dẫn tới tệp logo
        if not os.path.exists(logo_path):  # Kiểm tra xem tệp có tồn tại không
            raise FileNotFoundError(f"File not found: {logo_path}")  # Hiển thị lỗi nếu không tìm thấy tệp
        logo_image = Image.open(logo_path)  # Mở tệp hình ảnh logo
        logo_image = logo_image.resize((40, 40), Image.LANCZOS)  # Thay đổi kích thước hình ảnh
        self.logo_dash = ImageTk.PhotoImage(logo_image)  # Chuyển đổi hình ảnh sang định dạng Tkinter

        # === TITLE ===
        title = Label(self.root, text="Student Management System", image=self.logo_dash, padx=10, compound=LEFT,
                      bg="#1C2442", fg="white", font=("Arial", 24, "bold"))  # Tạo nhãn tiêu đề
        title.place(x=0, y=0, relwidth=1, height=80)  # Đặt vị trí và kích thước cho tiêu đề

        # === MENU === 
        M_Frame = LabelFrame(self.root, text="Menu", bg="white", font=("Arial", 12, "bold"))  # Tạo khung menu
        M_Frame.place(x=0, y=80, width=200, relheight=1)  # Đặt vị trí và kích thước cho khung menu

        # Thêm các nút vào khung menu
        self.create_menu_button(M_Frame, "Manage", self.manage, 0)  # Nút quản lý
        self.create_menu_button(M_Frame, "View", self.show_view, 75)  # Nút xem
        self.create_menu_button(M_Frame, "Logout", self.logout, 150)  # Nút đăng xuất
        self.create_menu_button(M_Frame, "Exit", self.exit_program, 220)  # Nút thoát

        # === MAIN FRAME ===
        self.bg_Home = Image.open("images/bg_home.png")  # Mở tệp hình nền
        self.bg_Home = self.bg_Home.resize((1150, 700), Image.LANCZOS)  # Thay đổi kích thước hình nền
        self.bg_Home = ImageTk.PhotoImage(self.bg_Home)  # Chuyển đổi hình nền sang định dạng Tkinter
        Label(self.root, image=self.bg_Home).place(x=200, y=80, relwidth=1, relheight=1)  # Đặt hình nền vào cửa sổ

    def create_menu_button(self, parent, text, command, y_position):
        """Hàm để tạo nút trong khung menu."""
        button = Button(parent, text=text, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)  # Tạo nút
        button.place(x=0, y=y_position, width=200, height=50)  # Đặt vị trí và kích thước cho nút
        button.bind("<Enter>", lambda e: button.config(bg="#3B3F4C"))  # Đổi màu nền khi chuột vào nút
        button.bind("<Leave>", lambda e: button.config(bg="#242533"))  # Khôi phục màu nền khi chuột ra
        return button  # Trả về nút

    def manage(self):
        """Hàm để mở trang quản lý sinh viên."""
        self.root.destroy()  # Đóng cửa sổ hiện tại
        open_manage_page()  # Mở cửa sổ quản lý trong manage_page.py

    def show_view(self):
        """Hàm cho chức năng xem thông tin sinh viên."""
        messagebox.showinfo("View", "Chức năng này đang được phát triển.")  # Hiển thị thông báo

    def logout(self):
        """Hàm để đăng xuất khỏi hệ thống."""
        if messagebox.askyesno("Logout", "Bạn có chắc chắn muốn đăng xuất?"):  # Hỏi người dùng có chắc chắn đăng xuất không
            self.root.destroy()  # Đóng cửa sổ hiện tại
            subprocess.run(["python", "gui/login_page.py"])  # Mở trang đăng nhập

    def exit_program(self):
        """Hàm để thoát khỏi chương trình."""
        if messagebox.askyesno("Exit", "Bạn có chắc chắn muốn thoát chương trình?"):  # Hỏi người dùng có muốn thoát không
            self.root.quit()  # Thoát chương trình

if __name__ == "__main__":
    root = Tk()  # Tạo một cửa sổ mới
    app = Main(root)  # Khởi động ứng dụng với cửa sổ root
    root.mainloop()  # Bắt đầu vòng lặp chính của Tkinter
