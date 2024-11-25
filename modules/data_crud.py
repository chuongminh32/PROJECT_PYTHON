import csv # Thư viện xử lý file CSV
import os
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
def read_data(file_path):
    """
    Đọc dữ liệu từ file CSV và trả về DataFrame.
    """
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv(file_path, encoding='utf-8') 

        if df.empty:  # Kiểm tra nếu dữ liệu trống
            messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
            return None

        return df

    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        return None
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi đọc file: {e}")
        return None

def create_data(student_data, file_path):
    """Thêm dữ liệu sinh viên vào file CSV, đảm bảo tiêu đề cột luôn đứng đầu."""
    # Đọc dữ liệu hiện tại trong file
    current_data = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file) # Đọc file CSV
            current_data = list(reader) # Chuyển dữ liệu sang list
    except FileNotFoundError:
        # Nếu file không tồn tại, tạo một danh sách rỗng
        pass

    # Kiểm tra xem tiêu đề đã có trong dữ liệu chưa
    if not current_data: 
        # Nếu không có dữ liệu, thêm tiêu đề
        current_data.append(["ID", "Name", "Nationality", "City", "Latitude", "Longitude", "Gender",
                             "Ethnic Group", "Age", "English Grade", "Math Grade", 
                             "Sciences Grade", "Language Grade", "Portfolio Rating", 
                             "Cover Letter Rating", "Reference Letter Rating"])

    # Thêm dữ liệu mới vào cuối danh sách (bỏ qua tiêu đề)      
    current_data.append(student_data)

    # Ghi lại toàn bộ dữ liệu vào file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(current_data)

def update_data(student_id, new_info):
    """Cập nhật thông tin sinh viên trong file CSV."""
    updated = False

    # Đọc dữ liệu từ file CSV
    with open("data/data_clean.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader) # rows 

    # duyet qua tung dong trong df va lay du lieu cot dau tien (id)
    for index, row in enumerate(rows): # Duyệt qua từng hàng
        if str(row[0]).strip() == student_id.strip():  # Kiểm tra ID sinh viên
            # Cập nhật thông tin mới, giữ ID trong cột đầu tiên
            rows[index] = [student_id] + new_info[1:]  # Giữ lại ID và thay thế các trường còn lại
            updated = True
            break
    # Nếu tìm thấy và cập nhật thành công, ghi dữ liệu vào file
    if updated:
        with open("data/data_clean.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return True
    else:
        return False

def delete_data(df, student_id):
    """
    Xóa sinh viên khỏi DataFrame dựa trên ID.
    """
    index = df[df['id'].astype(str) == student_id].index  # Chuyển ID sang chuỗi để so sánh
    if not index.empty:
        df = df.drop(index)  # Xóa dòng dữ liệu có ID trùng khớp
        return df
    else:
        return None  # Trả về None nếu không tìm thấy sinh viên