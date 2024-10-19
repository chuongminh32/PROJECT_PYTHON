import pandas as pd

def read_data(file_path):
    """
    Đọc dữ liệu từ file CSV.

    Hàm này sẽ cố gắng đọc dữ liệu từ file CSV tại đường dẫn 'file_path' và trả về DataFrame.
    Nếu xảy ra lỗi trong quá trình đọc, hàm sẽ bắt lỗi và trả về None.

    Parameters:
    file_path (str): Đường dẫn tới file CSV.

    Returns:
    DataFrame: DataFrame chứa dữ liệu từ file CSV.
    None: Nếu có lỗi xảy ra trong quá trình đọc file.
    """
    try:
        df = pd.read_csv(file_path, delimiter=';')  # Đọc file CSV vào DataFrame với dấu phân cách là dấu chấm phẩy
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")  # Thông báo lỗi nếu có sự cố
        return None

def add_data(df, new_row):
    """
    Thêm một hàng dữ liệu mới vào DataFrame.

    Hàm này nhận DataFrame hiện tại và một hàng dữ liệu mới (new_row) dạng dictionary,
    sau đó thêm hàng này vào cuối DataFrame.

    Parameters:
    df (DataFrame): DataFrame hiện tại chứa dữ liệu.
    new_row (dict): Hàng dữ liệu mới dưới dạng dictionary.

    Returns:
    DataFrame: DataFrame sau khi đã thêm hàng mới.
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
        df.loc[index] = pd.Series(updated_row)  # Cập nhật dòng với dữ liệu mới
    else:
        print(f"Không tìm thấy Student ID {student_id}")  # Thông báo nếu Student ID không tồn tại
    return df

def delete_data(df, student_id):
    """
    Xóa một hàng dữ liệu trong DataFrame theo Student ID.

    Hàm này tìm dòng có Student ID tương ứng và xóa dòng đó khỏi DataFrame.
    Nếu không tìm thấy Student ID, sẽ in ra thông báo lỗi.

    Parameters:
    df (DataFrame): DataFrame hiện tại chứa dữ liệu.
    student_id (str/int): Student ID của sinh viên cần xóa.

    Returns:
    DataFrame: DataFrame sau khi đã xóa hàng dữ liệu.
    """
    index = df[df['Student ID'] == student_id].index  # Tìm chỉ mục của dòng có Student ID
    if not index.empty:
        df = df.drop(index)  # Xóa dòng với Student ID tương ứng
        print(f"Đã xóa sinh viên với Student ID {student_id}")  # Thông báo đã xóa thành công
    else:
        print(f"Không tìm thấy Student ID {student_id}")  # Thông báo nếu Student ID không tồn tại
    return df

# Phần kiểm thử
if __name__ == "__main__":
    # Đường dẫn đến file CSV
    file_path =  r"G:\NamII_HK1\PY\PROJECT\PROJECT_PYTHON\data\data_demo.csv"   # Thay đổi đường dẫn theo file thực tế của bạn

    # Đọc dữ liệu từ file CSV
    df = read_data(file_path)

    # Kiểm tra dữ liệu đã đọc
    if df is not None:
        print("Dữ liệu ban đầu:")
        print(df)

        # Thêm một hàng dữ liệu mới
        new_row = {'Student ID': 1000, 'Student Country': 'Vietnam', 'Question ID': 78,
                   'Type of Answer': 1, 'Question Level': 'Basic', 'Topic': 'Statistics',
                   'Subtopic': 'Statistics', 'Keywords': 'Mean, Median'}
        df = add_data(df, new_row)
        print("\nDữ liệu sau khi thêm:")
        print(df)

        # Cập nhật một hàng dữ liệu
        updated_row = {'Student ID': 1000, 'Student Country': 'Vietnam', 'Question ID': 78,
                       'Type of Answer': 1, 'Question Level': 'Basic', 'Topic': 'Statistics',
                       'Subtopic': 'Statistics', 'Keywords': 'Variance, Standard Deviation'}
        df = update_data(df, 1000, updated_row)
        print("\nDữ liệu sau khi cập nhật:")
        print(df)

        # Xóa một hàng dữ liệu
        df = delete_data(df, 1000)
        print("\nDữ liệu sau khi xóa:")
        print(df)

        # Lưu dữ liệu đã xử lý (tùy chọn)
        # df.to_csv('data/cleaned_data.csv', sep=';', index=False)  # Lưu lại dữ liệu đã thay đổi
