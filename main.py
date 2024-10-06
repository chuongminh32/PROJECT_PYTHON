import sys
import os

# Thêm thư mục gốc của dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from modules.data_crud import read_data, add_data, update_data, delete_data, save_data
from modules.data_cleaning import remove_missing_values, remove_duplicates, correct_formatting
from modules.data_visualization import plot_average_scores
from modules.data_normalize import normalize_scores
from gui.main_gui import run_gui  # Nhập hàm chạy GUI từ main_gui.py

FILE_PATH = 'data/dataset.csv'

def main():
    # Đọc dữ liệu từ file CSV
    df = read_data(FILE_PATH)
    
    if df is not None:
        # Làm sạch dữ liệu
        df = remove_missing_values(df)
        df = remove_duplicates(df)
        df = correct_formatting(df)
        
        # Chuẩn hóa dữ liệu
        df = normalize_scores(df)
        
        # Thêm một dòng dữ liệu mới
        new_row = {
            'sbd': 100004, 'toan': 7.5, 'ngu_van': 6.0, 'ngoai_ngu': 8.0, 'vat_li': 7.0,
            'hoa_hoc': 6.5, 'sinh_hoc': 7.5, 'lich_su': 5.5, 'dia_li': 6.0, 'gdcd': 7.0,
            'ma_ngoai_ngu': 102
        }
        df = add_data(df, new_row)
        
        # Cập nhật dữ liệu của học sinh
        updated_row = {
            'sbd': 100002, 'toan': 6.5, 'ngu_van': 5.8, 'ngoai_ngu': 6.2, 'vat_li': 7.0,
            'hoa_hoc': 6.8, 'sinh_hoc': 7.0, 'lich_su': 4.5, 'dia_li': 6.5, 'gdcd': 7.0,
            'ma_ngoai_ngu': 102
        }
        df = update_data(df, 100002, updated_row)
        
        # Xóa dữ liệu của học sinh có SBD 100003
        df = delete_data(df, 100003)
        
        # Lưu dữ liệu lại vào file CSV
        save_data(df, FILE_PATH)
        
        # Vẽ biểu đồ điểm trung bình các môn
        plot_average_scores(df)

    # Chạy giao diện
    run_gui()

if __name__ == '__main__':
    main()
