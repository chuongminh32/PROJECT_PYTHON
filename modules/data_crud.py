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
        df = pd.read_csv(file_path, delimiter=',')  # Đọc file CSV với dấu phân cách là dấu phẩy
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
    df = df.append(new_row, ignore_index=True)  # Thêm hàng mới vào DataFrame và bỏ qua chỉ mục cũ
    return df

def update_data(df, sbd, updated_row):
    """
    Cập nhật dữ liệu trong DataFrame theo Số báo danh (sbd).

    Hàm này tìm dòng có sbd tương ứng và cập nhật toàn bộ dòng đó với dữ liệu từ updated_row.
    Nếu không tìm thấy sbd, sẽ in ra thông báo lỗi.

    Parameters:
    df (DataFrame): DataFrame hiện tại chứa dữ liệu.
    sbd (str/int): Số báo danh của sinh viên cần cập nhật.
    updated_row (dict): Dữ liệu cập nhật dưới dạng dictionary.

    Returns:
    DataFrame: DataFrame sau khi cập nhật dữ liệu.
    """
    index = df[df['sbd'] == sbd].index  # Tìm chỉ mục của dòng có sbd
    if not index.empty:
        df.loc[index, :] = updated_row  # Cập nhật dòng với dữ liệu mới
    else:
        print(f"Không tìm thấy SBD {sbd}")  # Thông báo nếu sbd không tồn tại
    return df

def delete_data(df, sbd):
    """
    Xóa một hàng dữ liệu trong DataFrame theo Số báo danh (sbd).

    Hàm này tìm dòng có sbd tương ứng và xóa dòng đó khỏi DataFrame.
    Nếu không tìm thấy sbd, sẽ in ra thông báo lỗi.

    Parameters:
    df (DataFrame): DataFrame hiện tại chứa dữ liệu.
    sbd (str/int): Số báo danh của sinh viên cần xóa.

    Returns:
    DataFrame: DataFrame sau khi đã xóa hàng dữ liệu.
    """
    index = df[df['sbd'] == sbd].index  # Tìm chỉ mục của dòng có sbd
    if not index.empty:
        df = df.drop(index)  # Xóa dòng với sbd tương ứng
        print(f"Đã xóa sinh viên với SBD {sbd}")  # Thông báo đã xóa thành công
    else:
        print(f"Không tìm thấy SBD {sbd}")  # Thông báo nếu sbd không tồn tại
    return df
