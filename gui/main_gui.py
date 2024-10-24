# from tkinter import *
# from PIL import Image, ImageTk
# import os

# class MainGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Hệ thống quản lý sinh viên")
        
#         # Đặt kích thước cửa sổ
#         self.root.geometry("1350x700+0+0")
#         # self.root.attributes('-fullscreen', True)  # Đặt cửa sổ ở chế độ toàn màn hình nếu cần
        
#         # Đặt màu nền cho cửa sổ
#         self.root.configure(background="#171823")

#         # === ICON === 
#         # Đường dẫn tuyệt đối đến tệp hình ảnh logo.png
#         logo_path = r"D:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\gui\images\logo2.png"
#         if not os.path.exists(logo_path):
#             raise FileNotFoundError(f"File not found: {logo_path}")
#         self.logo_dash = ImageTk.PhotoImage(file=logo_path)

#         # === TITLE ===
#         # Tạo tiêu đề với hình ảnh logo
#         title = Label(self.root, text="Student Management System", padx=10, compound=LEFT, image=self.logo_dash, bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
#         title.place(x=0, y=0, relwidth=1, height=50)

#         # === MENU === 
#         # Tạo khung menu bên trái
#         M_Frame = LabelFrame(self.root, text="Menu", bg="#1C2442", fg="white", font=("Arial", 12, "bold"))
#         M_Frame.place(x=0, y=50, width=200, relheight=1)

#         # Thêm các nút vào khung menu
#         btn_course = Button(M_Frame, text="Courses", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=0, width=200, height=50)
#         btn_student = Button(M_Frame, text="Student", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=60, width=200, height=50)
#         btn_result = Button(M_Frame, text="Result", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=120, width=200, height=50)
#         btn_view = Button(M_Frame, text="View", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=180, width=200, height=50)
#         btn_logout = Button(M_Frame, text="Logout", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=240, width=200, height=50)
#         btn_exit = Button(M_Frame, text="Exit", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=300, width=200, height=50)

#         # === CONTENT ===
#         # Đường dẫn tuyệt đối đến tệp hình ảnh bg.jpg
#         bg_path = r"D:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\gui\images\bg.jpg"
#         if not os.path.exists(bg_path):
#             raise FileNotFoundError(f"File not found: {bg_path}")
#         try:
#             # Mở và thay đổi kích thước hình nền
#             self.bg_img = Image.open(bg_path)
#             self.bg_img = self.bg_img.resize((1200, 600), Image.LANCZOS)
#             self.bg_img = ImageTk.PhotoImage(self.bg_img)
#         except Exception as e:
#             raise UnidentifiedImageError(f"Cannot identify image file: {bg_path}") from e

#         # Đặt hình nền vào giữa cửa sổ
#         self.lgl_bg = Label(self.root, image=self.bg_img)
#         self.lgl_bg.place(x=210, y=60, width=1200, height=600)

#         #update_detail
#         self.lbl_course = Label(self.root, text="Total Courses\n[0]", bg="#121927", fg="white", font=("Arial", 20, "bold"), relief=RIDGE, bd=10)
#         self.lbl_course.place(x=450, y=680, width=200, height=150)
#         # self.lbl_course = Label(self.root, text="Total Courses\n[0]", bg="#121927", fg="white", font=("Arial", 20, "bold"))
#         # self.lbl_course.place(x=400, y=680, width=200, height=150)
#         # self.lbl_course = Label(self.root, text="Total Courses\n[0]", bg="#121927", fg="white", font=("Arial", 20, "bold"))
#         # self.lbl_course.place(x=400, y=680, width=200, height=150)  
# if __name__ == "__main__":
#     root = Tk()
#     app = MainGUI(root)
#     root.mainloop()


from tkinter import *
from PIL import Image, ImageTk
import os

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
        # size  
        self.root.geometry("1350x700+0+0")
        # self.root.attributes('-fullscreen', True)
        # màu nền
        self.root.configure(background="#171823")

        # === ICON === 
        # Đường dẫn tuyệt đối đến tệp hình ảnh logo.png
        logo_path = r"D:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\gui\images\logo2.png"
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"File not found: {logo_path}")
        
        # Mở và thay đổi kích thước hình ảnh logo
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((30, 30), Image.LANCZOS)  # Thay đổi kích thước logo (100x100 là kích thước mới)
        self.logo_dash = ImageTk.PhotoImage(logo_img)

        # === TITLE ===
        # Tạo tiêu đề với hình ảnh logo
        title = Label(self.root, text="Student Management System", padx=10, compound=LEFT, image=self.logo_dash, bg="#1C2442", fg="white", font=("Arial", 24, "bold"))
        title.place(x=0, y=0, relwidth=1, height=50)

        # === MENU === 
        # Tạo khung menu bên trái
        M_Frame = LabelFrame(self.root, text="Menu", bg="#1C2442", fg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=50, width=200, relheight=1)

        # Thêm các nút vào khung menu
        btn_course = Button(M_Frame, text="Courses", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=0, width=200, height=50)
        btn_student = Button(M_Frame, text="Student", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=60, width=200, height=50)
        btn_result = Button(M_Frame, text="Result", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=120, width=200, height=50)
        btn_view = Button(M_Frame, text="View", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=180, width=200, height=50)
        btn_logout = Button(M_Frame, text="Logout", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=240, width=200, height=50)
        btn_exit = Button(M_Frame, text="Exit", bg="#242533", fg="white", font=("Arial", 12, "bold")).place(x=0, y=300, width=200, height=50)

        # === CONTENT ===
        bg_path = r"D:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\gui\images\bg.jpg"
        if not os.path.exists(bg_path):
            raise FileNotFoundError(f"File not found: {bg_path}")
        try:
            # Mở và thay đổi kích thước hình nền
            self.bg_img = Image.open(bg_path)
            self.bg_img = self.bg_img.resize((1200, 600), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
        except Exception as e:
            raise UnidentifiedImageError(f"Cannot identify image file: {bg_path}") from e

        # Đặt hình nền vào giữa cửa sổ
        self.lgl_bg = Label(self.root, image=self.bg_img)
        self.lgl_bg.place(x=200, y=60, width=1200, height=600)

if __name__ == "__main__":
    root = Tk()
    app = MainGUI(root)
    root.mainloop()