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
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    return df

def update_data(df, sbd, updated_row):
    """
    Cập nhật dữ liệu theo SBD.
    """
    index = df[df['sbd'] == sbd].index
    if not index.empty:
        for key in updated_row:
            if key in df.columns:
                df.loc[index, key] = updated_row[key]
    else:
        print(f"Không tìm thấy SBD {sbd}")
    return df

def delete_data(df, sbd):
    """
    Xóa hàng dữ liệu theo SBD.
    """
    index = df[df['sbd'] == sbd].index
    if not index.empty:
        df = df.drop(index)
        print(f"Đã xóa SBD {sbd}")
    else:
        print(f"Không tìm thấy SBD {sbd}")
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
        new_row = {'sbd': '01000008', 'toan': 9.0, 'ngu_van': 8.5, 'ngoai_ngu': 8.0, 'vat_li': 7.0,
                   'hoa_hoc': 6.5, 'sinh_hoc': 5.5, 'lich_su': 6.0, 'dia_li': 7.5, 'gdcd': 8.0, 'ma_ngoai_ngu': 'N2'}
        df = add_data(df, new_row)
        print("\nDữ liệu sau khi thêm:")
        print(df)

        # Cập nhật một hàng dữ liệu
        updated_row = {'sbd': '01000008', 'toan': 9.5, 'ngu_van': 8.75, 'ngoai_ngu': 8.2, 'vat_li': 7.2,
                       'hoa_hoc': 6.8, 'sinh_hoc': 5.8, 'lich_su': 6.5, 'dia_li': 7.8, 'gdcd': 8.2, 'ma_ngoai_ngu': 'N2'}
        df = update_data(df, '01000008', updated_row)
        print("\nDữ liệu sau khi cập nhật:")
        print(df)

        # Xóa một hàng dữ liệu
        df = delete_data(df, '01000008')
        print("\nDữ liệu sau khi xóa:")
        print(df)

        # Lưu dữ liệu đã thay đổi vào file mới
        df.to_csv(output_file_path, sep=',', index=False)
        print(f"\nDữ liệu đã được lưu vào {output_file_path}")
