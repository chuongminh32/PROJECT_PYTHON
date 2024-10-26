import pandas as pd

def read_data(file_path):
    """
    Đọc dữ liệu từ file CSV.
    """
    try:
        df = pd.read_csv(file_path, delimiter=',')
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

def add_data(df, new_row):
    """
    Thêm hàng mới vào DataFrame.
    """
    new_row_df = pd.DataFrame([new_row])  # Chuyển dictionary thành DataFrame
    df = pd.concat([df, new_row_df], ignore_index=True)  # Thêm hàng mới vào DataFrame
    return df
def update_data(df, student_id, updated_row):
    """
    Cập nhật dữ liệu trong DataFrame theo Student ID.

    Hàm này tìm dòng có Student ID tương ứng và cập nhật toàn bộ dòng đó với dữ liệu từ updated_row.
    Nếu không tìm thấy Student ID, sẽ in ra thông báo lỗi.

    Parameters:
    df (DataFrame): DataFrame hiện tại chứa dữ liệu.
    student_id (str/int): Student ID của sinh viên cần cập nhật.
    updated_row (dict): Dữ liệu cập nhật dưới dạng dictionary.

    Returns:
    DataFrame: DataFrame sau khi cập nhật dữ liệu.
    """
    index = df[df['Student ID'] == student_id].index  # Tìm chỉ mục của dòng có Student ID
    if not index.empty:
        # Đảm bảo rằng các giá trị của updated_row được ánh xạ đúng với cột của DataFrame
        for key in updated_row:
            if key in df.columns:
                df.loc[index, key] = updated_row[key]
    else:
        print(f"Không tìm thấy Student ID {student_id}")  # Thông báo nếu Student ID không tồn tại
    return df

def update_data(df, id, updated_row):
    """
    Cập nhật dữ liệu theo ID.
    """
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
    index = df[df['id'] == id].index
    if not index.empty:
        df = df.drop(index)
        print(f"Đã xóa ID {id}")
    else:
        print(f"Không tìm thấy ID {id}")
    return df

# Phần kiểm thử
if __name__ == "__main__":
    # Đường dẫn đến file CSV gốc và file lưu kết quả
    input_file_path = r"D:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\data\data_demo.csv"  # Đường dẫn file CSV gốc
    output_file_path = r"D:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\data\data_clean.csv"  # Đường dẫn lưu kết quả

    # Đọc dữ liệu từ file CSV
    df = read_data(input_file_path)

    # Kiểm tra dữ liệu đã đọc
    if df is not None:
        print("Dữ liệu ban đầu:")
        print(df)

        # Thêm một hàng dữ liệu mới
        new_row = {'id': 8, 'name': 'Minh Chuong', 'nationality': 'Vietnam', 'city': 'Hanoi', 'latitude': 21.02, 'longitude': 105.84,
                   'gender': 'F', 'ethnic.group': 'NA', 'age': 23, 'english.grade': 4.0, 'math.grade': 4.5, 'sciences.grade': 4.2,
                   'language.grade': 3, 'portfolio.rating': 4, 'coverletter.rating': 4, 'refletter.rating': 4}
        df = add_data(df, new_row)
        print("\nDữ liệu sau khi thêm:")
        print(df)

        # Cập nhật một hàng dữ liệu
        updated_row = {'name': 'Chuong Minh', 'nationality': 'Vietnam', 'city': 'Hanoi', 'latitude': 21.02, 'longitude': 105.84,
                       'gender': 'F', 'ethnic.group': 'NA', 'age': 23, 'english.grade': 4.5, 'math.grade': 4.8, 'sciences.grade': 4.5,
                       'language.grade': 3.5, 'portfolio.rating': 4.5, 'coverletter.rating': 4.5, 'refletter.rating': 4.5}
        df = update_data(df, 8, updated_row)
        print("\nDữ liệu sau khi cập nhật:")
        print(df)

        # Xóa một hàng dữ liệu
        df = delete_data(df, 8)
        print("\nDữ liệu sau khi xóa:")
        print(df)

        # Lưu dữ liệu đã thay đổi vào file mới
        df.to_csv(output_file_path, sep=',', index=False)
        print(f"\nDữ liệu đã được lưu vào {output_file_path}")