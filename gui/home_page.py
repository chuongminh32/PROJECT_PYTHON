from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

class HomePage:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_logo()
        self.create_menu()

    def setup_window(self):
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1000x550+300+200")
        self.root.configure(background="white")
        self.root.resizable(False, False)

    def create_logo(self):
        logo_path = os.path.join("images", "logo_fit.png")
        logo_image = Image.open(logo_path).resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo_image)
        Label(self.root, text="Trang chủ", image=self.logo_dash, padx=10, compound=LEFT,
              bg="#1C2442", fg="white", font=("Arial", 24, "bold")).place(x=0, y=0, relwidth=1, height=80)

    def create_menu(self):
        M_Frame = LabelFrame(self.root, text="Menu", bg="white", font=("Arial", 12, "bold"))
        M_Frame.place(x=0, y=80, width=200, relheight=1)
        menu_items = [("Quản lí", self.manage), ("Trực quan", self.show_view), 
                      ("Sinh viên", self.stu), ("Đăng xuất", self.logout), ("Thoát", self.exit_program)]
        for i, (text, command) in enumerate(menu_items):
            self.create_menu_button(M_Frame, text, command, i * 75)
        self.bg_Home = ImageTk.PhotoImage(Image.open("images/bg_home.png").resize((800, 470), Image.LANCZOS))
        Label(self.root, image=self.bg_Home).place(x=200, y=80, width=800, height=470)

    def create_menu_button(self, parent, text, command, y_position):
        button = Button(parent, text=text, border=0, bg="#242533", fg="white", font=("Arial", 12, "bold"), command=command)
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
