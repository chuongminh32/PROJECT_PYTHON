from tkinter import messagebox
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
    try:
        # Đọc dữ liệu hiện tại trong file
        df = pd.read_csv(file_path, encoding='utf-8')
    except FileNotFoundError:
        # Nếu file không tồn tại, tạo một DataFrame mới với tiêu đề cột
        columns = ["ID", "Name", "Nationality", "City", "Latitude", "Longitude", "Gender",
                   "Ethnic Group", "Age", "English Grade", "Math Grade",
                   "Sciences Grade", "Language Grade", "Portfolio Rating",
                   "Cover Letter Rating", "Reference Letter Rating"]
        df = pd.DataFrame(columns=columns)

    # Thêm dữ liệu mới vào DataFrame
    df = pd.concat([df, pd.DataFrame([student_data], columns=df.columns)], ignore_index=True)

    # Ghi lại toàn bộ dữ liệu vào file
    df.to_csv(file_path, index=False, encoding='utf-8')

def update_data(file_path, student_id, new_info):
    """Cập nhật thông tin sinh viên trong file CSV."""
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv(file_path, encoding='utf-8')

        # Tìm chỉ số của sinh viên cần cập nhật
        index = df[df['id'].astype(str) == student_id].index
        if not index.empty:
            # Cập nhật thông tin mới
            for i, col in enumerate(df.columns):
                df.at[index[0], col] = new_info[i]
            # Ghi lại toàn bộ dữ liệu vào file
            df.to_csv(file_path, index=False, encoding='utf-8')
            return True
        else:
            return False
    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        return False
    except Exception as e:
        print(e)
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi cập nhật dữ liệu: {e}")
        return False

def delete_data(file_path, student_id):
    """
    Xóa sinh viên khỏi DataFrame dựa trên ID.
    """
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv(file_path, encoding='utf-8')

        # Tìm chỉ số của sinh viên cần xóa
        index = df[df['id'].astype(str) == student_id].index

        if not index.empty:
            # Xóa dòng dữ liệu có ID trùng khớp
            df = df.drop(index)
            # Ghi lại toàn bộ dữ liệu vào file
            df.to_csv(file_path, index=False, encoding='utf-8')
            return True
        else:
            return False
    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy file: {file_path}")
        return False
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi xóa dữ liệu: {e}")
        return False