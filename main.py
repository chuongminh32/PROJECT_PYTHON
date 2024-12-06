# import subprocess # Thư viện subprocess giúp chạy lệnh terminal từ Python
# import sys # Thư viện sys giúp truy cập các biến môi trường và hàm tương tác với hệ thống

# # Danh sách các thư viện cần cài đặt
# REQUIRED_LIBRARIES = [
#     "pandas",
#     "matplotlib",
#     "tkinter",  # tkinter là thư viện mặc định, không cần cài đặt với Python >= 3
#     "Pillow",  # thư viện PIL đã được đổi tên thành Pillow
# ]

# # Hàm tự động cài đặt các thư viện thiếu
# def install_requirements():
#     for lib in REQUIRED_LIBRARIES:
#         try:
#             __import__(lib)  # Kiểm tra xem thư viện đã được cài chưa
#             print(f"{lib} is already installed.")
#         except ImportError:
#             print(f"Missing library: {lib}, installing...")
#             subprocess.check_call([sys.executable, "-m", "pip", "install", lib])  # Cài đặt thư viện

#     print("All libraries are installed and ready to use!")

# # Sau khi cài đặt xong, khởi động ứng dụng
# def run_application():
#     from tkinter import Tk  # Import Tkinter sau khi cài đặt
#     from gui.login_page import LoginPage  # Import lớp LoginPage từ file login_page.py
    
#     root = Tk()  # Khởi tạo cửa sổ chính của ứng dụng
#     app = LoginPage(root)  # Tạo đối tượng lớp LoginPage
#     root.mainloop()  # Chạy ứng dụng Tkinter

# # Khởi động quá trình cài đặt và chạy ứng dụng
# if __name__ == "__main__":
#     install_requirements()  # Cài đặt thư viện nếu thiếu
#     run_application()  # Khởi động ứng dụng sau khi cài đặt xong


def plot_grade_btn(FILE_PATH):
    plt.close('all')
    df = pd.read_csv(FILE_PATH)
    subject = ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']
    grade = df[subject].mean()

    plt.figure(figsize=(10,6))
    plt.bar(subject, grade)
    plt.xlabel("Môn học")
    plt.ylabel("Điểm")
    plt.title("Biều đồ điểm trung bình môn học")

    for i, value in enumerate(grade):
        plt.text(i, value + 0.05, round(value, 2), ha='center', va='bottom')

    plt.show()

if __name__ == '__main__':
    plot_grade_btn("data/student-dataset.csv")