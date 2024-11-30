import unittest
import os
import pandas as pd
import traceback
from tkinter import Tk
from unittest.mock import patch
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_crud import read_data, create_data, update_data, delete_data

class TestCSVOperationsDetailed(unittest.TestCase):
    def setUp(self):
        """
        Tạo dữ liệu và file CSV giả lập trước mỗi test.
        """
        self.file_path = 'test_data.csv'
        self.sample_data = pd.DataFrame({
            "id": [1, 2],
            "name": ["Alice", "Bob"],
            "nationality": ["Country A", "Country B"],
            "city": ["City A", "City B"],
            "latitude": [1.0, 2.0],
            "longitude": [3.0, 4.0],
            "gender": ["F", "M"],
            "ethnic.group": ["Group A", "Group B"],
            "age": [25, 30],
            "english.grade": [4.0, 3.5],
            "math.grade": [3.8, 3.9],
            "sciences.grade": [4.0, 4.0],
            "language.grade": [3.6, 3.7],
            "portfolio.rating": [4, 5],
            "coverletter.rating": [4.2, 3.8],
            "refletter.rating": [3.9, 4.1]
        })
        self.sample_data.to_csv(self.file_path, index=False, encoding='utf-8')

    def tearDown(self):
        """
        Xóa file CSV giả lập sau mỗi test.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    @patch("tkinter.messagebox.showerror")
    def test_read_data_error_handling(self, mock_error):
        """
        Hàm test_read_data_error_handling:
        Hàm này kiểm tra lỗi khi đọc file CSV không tồn tại.
        Kết quả cho thấy hàm read_data ném ra lỗi FileNotFoundError
        và hiển thị thông báo lỗi qua tkinter.messagebox với nội dung:
        "Không tìm thấy file: non_existent.csv".
        Test sử dụng mock_error để xác nhận rằng thông báo lỗi được gọi đúng cách. 
        Kết luận, hàm đã xử lý lỗi đọc file chính xác khi file không tồn tại.
        Test báo lỗi cụ thể khi xảy ra lỗi đọc file.
        """
        try:
            # Gọi hàm với đường dẫn không tồn tại
            read_data("non_existent.csv")
        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()  # In chi tiết lỗi ra màn hình
        mock_error.assert_called_once()
        mock_error.assert_called_with("Lỗi", "Không tìm thấy file: non_existent.csv")

    def test_create_data_empty_columns(self):
        """
        Hàm test_create_data_empty_columns:
        Hàm kiểm tra trường hợp dữ liệu đầu vào không đủ số cột.
        Khi gọi create_data với dữ liệu thiếu cột, hàm ném ra lỗi ValueError
        cùng thông báo: "Số lượng dữ liệu (4) không khớp với số cột (16).".
        Sử dụng assertRaises để kiểm tra lỗi này được xử lý đúng như mong đợi. 
        Kết luận, hàm đã hoạt động chính xác, không cho phép thêm dữ liệu không đầy đủ.
        Test lỗi khi thiếu cột trong dữ liệu.
        """
        incomplete_student = [3, "Charlie", "Country C", "City C"]  # Dữ liệu không đủ số cột
        with self.assertRaises(ValueError) as context:
            create_data(incomplete_student, self.file_path)

        # Kiểm tra thông báo lỗi
        self.assertEqual(
            str(context.exception),
            "Số lượng dữ liệu (4) không khớp với số cột (16)."
        )
    def test_update_data_invalid_id(self):
        """

        Hàm test_update_data_invalid_id:
        Hàm này kiểm tra việc cập nhật dữ liệu với ID không tồn tại trong file CSV. 
        Kết quả cho thấy hàm update_data trả về False khi không tìm thấy ID cần cập nhật,
        và không có lỗi bất ngờ xảy ra. Điều này chứng minh rằng hàm đã xử lý chính xác 
        trường hợp ID không tồn tại mà không làm ảnh hưởng đến dữ liệu.
        Test báo lỗi khi cập nhật với ID không tồn tại.
        """
        try:
            # Cập nhật thông tin với ID không tồn tại
            new_info = [3, "Updated Name", "Updated Country", "Updated City", 0, 0, "M", "Group", 20, 3.5, 3.5, 3.5, 3.5, 3, 3.5, 3]
            result = update_data(self.file_path, "999", new_info)
            self.assertFalse(result, "Update should fail for non-existent ID.")
        except Exception as e:
            print("Error occurred while updating:", str(e))
            traceback.print_exc()
            self.fail(f"Error when updating data: {e}")

    @patch("tkinter.messagebox.showerror")
    def test_delete_data_invalid_file(self, mock_error):
        """
        Hàm test_delete_data_invalid_file:
        Hàm kiểm tra lỗi khi xóa dữ liệu từ một file CSV không tồn tại. 
        Kết quả cho thấy hàm delete_data ném lỗi và hiển thị thông báo qua tkinter
        .messagebox với nội dung: "Không tìm thấy file: invalid_file.csv".
        Test sử dụng mock_error để đảm bảo thông báo được gọi một cách chính xác. 
         Kết luận, hàm xử lý lỗi đọc file chính xác khi file không tồn tại.
        Test lỗi khi xóa dữ liệu từ file không tồn tại.
        """
        try:
            # Xóa dữ liệu từ file không tồn tại
            result = delete_data("invalid_file.csv", "1")
            self.assertFalse(result)
        except Exception as e:
            print("Error occurred while deleting:", str(e))
            traceback.print_exc()
        mock_error.assert_called_once()
        mock_error.assert_called_with("Lỗi", "Không tìm thấy file: invalid_file.csv")

    def test_delete_data_invalid_id(self):
        """
        Hàm test_delete_data_invalid_id:
        Hàm kiểm tra việc xóa dữ liệu với ID không tồn tại trong file CSV. 
        Khi gọi delete_data với một ID không tồn tại, hàm trả về False và không gây
        ra lỗi nào khác. Điều này cho thấy hàm xử lý chính xác, không thực hiện thao
        tác xóa khi ID không tồn tại.
        Test lỗi khi ID không tồn tại trong file CSV.
        """
        try:
            result = delete_data(self.file_path, "999")  # ID không tồn tại
            self.assertFalse(result, "Delete should fail for non-existent ID.")
        except Exception as e:
            print("Error occurred while deleting:", str(e))
            traceback.print_exc()
            self.fail(f"Error when deleting data: {e}")

if __name__ == "__main__":
    # Tạo root Tkinter để chạy messagebox mà không lỗi
    root = Tk()
    root.withdraw()  # Ẩn cửa sổ Tkinter
    unittest.main()

