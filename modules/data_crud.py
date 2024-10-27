import pandas as pd
import csv
from tkinter import messagebox

def read_data(file_path="data/data_clean.csv"):
    """
    Đọc dữ liệu từ file CSV và trả về danh sách các hàng.
    
    Args:
        file_path (str): Đường dẫn đến file CSV.

    Returns:
        list: Danh sách các hàng dữ liệu từ file CSV hoặc None nếu có lỗi hoặc không có dữ liệu.
    """
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        if not data:  # Kiểm tra nếu dữ liệu trống
            messagebox.showinfo("Thông báo", "Không có dữ liệu để hiển thị.")
            return None

        return data

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
            reader = csv.reader(file)
            current_data = list(reader)
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

    # lấy data trong file demo  -> lưu list row 
    with open("data/data_clean.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Tìm kiếm ID sinh viên và cập nhật thông tin
    for index, row in enumerate(rows):
        # tìm data sinh viên theo ID (diuyệt qua tất cả các dòng | cột 0 trong data)
        if row[0] == student_id:  # Giả sử ID sinh viên nằm ở cột đầu tiên
            rows[index] = new_info  # Cập nhật thông tin mới
            updated = True
            break

    # Ghi dữ liệu cập nhật lại vào file
    if updated:
        with open("data/data_clean.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return True
    else:
        return False

def delete_data(df, student_id):
    """
    Xóa hàng dữ liệu theo ID.
    """
    index = df[df['id'].astype(str) == student_id].index  # Chuyển đổi ID sang chuỗi để so sánh
    if not index.empty:
        df = df.drop(index)  # Xóa hàng dữ liệu
        print(f"Đã xóa ID {student_id}")
    else:
        print(f"Không tìm thấy ID {student_id}")

    return df  # Trả về DataFrame đã cập nhật
