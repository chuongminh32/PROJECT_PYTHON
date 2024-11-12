import subprocess
import sys

# Danh sách các thư viện cần cài đặt
REQUIRED_LIBRARIES = [
    "pandas",
    "matplotlib",
    "tkinter",  # tkinter là thư viện mặc định, không cần cài đặt với Python >= 3
    "Pillow",  # thư viện PIL đã được đổi tên thành Pillow
]

# Hàm tự động cài đặt các thư viện thiếu
def install_requirements():
    for lib in REQUIRED_LIBRARIES:
        try:
            __import__(lib)  # Kiểm tra xem thư viện đã được cài chưa
            print(f"{lib} is already installed.")
        except ImportError:
            print(f"Missing library: {lib}, installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])  # Cài đặt thư viện

    print("All libraries are installed and ready to use!")

# Sau khi cài đặt xong, khởi động ứng dụng
def run_application():
    from tkinter import Tk  # Import Tkinter sau khi cài đặt
    from gui.login_page import LoginPage  # Import lớp LoginPage từ file login_page.py
    
    root = Tk()  # Khởi tạo cửa sổ chính của ứng dụng
    app = LoginPage(root)  # Tạo đối tượng lớp LoginPage
    root.mainloop()  # Chạy ứng dụng Tkinter

# Khởi động quá trình cài đặt và chạy ứng dụng
if __name__ == "__main__":
    install_requirements()  # Cài đặt thư viện nếu thiếu
    run_application()  # Khởi động ứng dụng sau khi cài đặt xong
