import sys
import os

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_gui import run_gui

def main():
    # Chạy giao diện chính của ứng dụng
    run_gui()

if __name__ == '__main__':
    main()
