import pandas as pd

def read_data(file_path):
    """
    Đọc dữ liệu từ file CSV và trả về DataFrame.
    """
    try:
        df = pd.read_csv(file_path, delimiter=',')
        if df.empty:  # Kiểm tra nếu dữ liệu trống
            print("Không có dữ liệu để hiển thị.")
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

def add_data(df, new_row):
    """
    Thêm hàng mới vào DataFrame.
    """
    if df is None:
        print("DataFrame is None. Cannot add data.")
        return df

    # Kiểm tra nếu dữ liệu mới có đúng số lượng cột như DataFrame
    if len(new_row) == len(df.columns):
        new_row_df = pd.DataFrame([new_row], columns=df.columns)
        df = pd.concat([df, new_row_df], ignore_index=True)
    else:
        print("Dữ liệu mới không khớp với cấu trúc DataFrame.")
    return df

def update_data(df, id, updated_row):
    """
    Cập nhật dữ liệu theo ID.
    """
    if df is None:
        print("DataFrame is None. Cannot update data.")
        return df

    index = df[df['id'] == id].index
    if not index.empty:
        for key in updated_row:
            if key in df.columns:
                df.loc[index, key] = updated_row[key]
    else:
        print(f"Không tìm thấy ID {id}")
    return df

def delete_data(df, id):
    """
    Xóa hàng dữ liệu theo ID.
    """
    if df is None:
        print("DataFrame is None. Cannot delete data.")
        return df

    index = df[df['id'] == id].index
    if not index.empty:
        df = df.drop(index)
        print(f"Đã xóa ID {id}")
    else:
        print(f"Không tìm thấy ID {id}")
    return df

# Ví dụ sử dụng:
if __name__ == "__main__":
    # Đường dẫn đến file CSV
    file_path = "data/data_demo.csv"

    # Đọc dữ liệu từ file CSV
    df = read_data(file_path)
    if df is not None:
        print("Dữ liệu ban đầu:")
        print(df)

        # Thêm hàng mới
        new_row = [8, "Alex Doe", "Canada", "Toronto", 43.7, -79.42, "M", "NA", 23, 3.0, 3.5, 3.8, 4, 3, 4, 5]
        df = add_data(df, new_row)
        print("\nDữ liệu sau khi thêm:")
        print(df)

        # Cập nhật hàng theo ID
        updated_row = {"name": "Alex Smith", "english.grade": 4.0}
        df = update_data(df, 8, updated_row)
        print("\nDữ liệu sau khi cập nhật:")
        print(df)

        # Xóa hàng theo ID
        df = delete_data(df, 8)
        print("\nDữ liệu sau khi xóa:")
        print(df)

        # Lưu dữ liệu đã thay đổi vào file mới
        output_file_path = "data/data_clean.csv"
        df.to_csv(output_file_path, sep=',', index=False)
        print(f"\nDữ liệu đã được lưu vào {output_file_path}")

        #  test 
# update_data("1", ["1", "Nguyễn Văn A", "Việt Nam", "Hà Nội", "21.028511", "105.804817", "Nam", "Kinh", "20", "8.0", "7.5", "8.0", "7.5", "8.0", "8.0", "8.0"])


# def display_data_in_table(root, data):
#     """
#     Hiển thị dữ liệu dưới dạng bảng trong Tkinter.
    
#     Args:
#         root (Tk): Cửa sổ Tkinter.
#         data (list): Danh sách các hàng dữ liệu để hiển thị.
#     """
#     if data is None or len(data) == 0:
#         return

#     # Tạo Treeview để hiển thị bảng dữ liệu
#     table = ttk.Treeview(root, columns=[f"col_{i}" for i in range(len(data[0]))], show='headings')
#     table.pack(expand=True, fill='both')

#     # Đặt tên cột theo hàng đầu tiên
#     for i, header in enumerate(data[0]):
#         table.heading(f"col_{i}", text=header)
#         table.column(f"col_{i}", width=100)  # Điều chỉnh độ rộng của cột

#     # Thêm các hàng dữ liệu
#     for row in data[1:]:  # Bỏ qua hàng đầu tiên (header)
#         table.insert("", "end", values=row)

# def main():
#     root = tk.Tk()
#     root.title("Hiển thị dữ liệu dạng bảng")
#     root.geometry("800x400")

#     # Đọc và hiển thị dữ liệu
#     data = read_data()
#     display_data_in_table(root, data)

#     root.mainloop()

# if __name__ == "__main__":
#     main()