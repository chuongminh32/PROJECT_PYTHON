# ĐỒ ÁN PYTHON 

### Thành viên 1
- **Họ và tên**: Phạm Hàn Minh Chương.
- **MSSV**: 23110187.
- **Vai trò**: Leader, Quản lí dự án, lên kế hoạch, điều phối nhóm, code GUI [FE].

### Thành viên 2
- **Họ và tên**: Nguyễn Thanh Bình Minh.
- **MSSV**: 23110266.
- **Vai trò**: BE, Code chức năng CRUD, làm sạch data.

### Thành viên 3
- **Họ và tên**: Nguyễn Thị Thanh Thùy.
- **MSSV**: 23110336.
- **Vai trò**: BE, Vẽ biểu đồ, chuẩn hóa thống nhất data, Tester.

* Cấu trúc thư mục đồ án:
    PROJECT_PYTHON/
    │
    ├── data/                           # Thư mục chứa tập tin dữ liệu
    │   ├── student-dataset.csv         # Tập dữ liệu nguồn
    │   ├── sorted_by_age.csv           # Tập dữ liệu săp xếp theo tuổi
    │   ├── sorted_by_gpa.csv           # Tập dữ liệu sắp xếp theo gpa
    │   ├── data_clean.csv              # Tập dữ liệu đã làm sạch (sau khi xử lý)
    │   └── users.txt                   # lưu trữ account
    │
    ├── modules/                        # Thư mục chứa các modules theo chức năng
    │   ├── __init__.py                 # Tập tin để biến "modules" thành một package
    │   ├── data_cleaning.py            # Module xử lý làm sạch dữ liệu
    │   ├── data_crud.py                # Module thực hiện các thao tác CRUD
    │   ├── data_visualization.py       # Module trực quan hóa dữ liệu
    │   └── student_function.py         # Module tính toán thống kê dữ liệu sinh viên (tính năng mới)
    │   
    │
    ├── gui/                             # Thư mục chứa các tập tin giao diện 
    │   ├── home_page.py                 # Trang chủ
    │   ├── login_page.py                # Trang đăng nhập
    │   ├── manage_page.py               # Trang quản lí [CRUD, CLEANINNG]
    │   ├── signup_page.py               # Trang đăng kí
    │   ├── student_page.py              # Trang xử lí liên quan đến sinh viên
    │   └── view_page.py                 # Trang trực quan [VISUALIZATION]
    │   
    ├── images/                         # Thư mục chứa các tập tin giao diện image
    │
    ├── tests/                          # Thư mục chứa các tập tin kiểm thử (optional)
    │   ├── test_cleaning.py            # Kiểm thử module làm sạch dữ liệu
    │   ├── test_crud.py                # Kiểm thử module CRUD
    │   └── test_visualization.py       # Kiểm thử module trực quan hóa dữ liệu
    │
    ├── main.py                         # Chương trình chính để chạy dự án
    ├── requirements.txt                # Danh sách thư viện phụ thuộc (Numpy, Pandas,...)
    └── README.md                       # Tập tin hướng dẫn sử dụng


# Hướng Dẫn Chạy Ứng Dụng

## Giới Thiệu

Ứng dụng này được xây dựng để cung cấp giao diện người dùng (GUI) sử dụng Tkinter và các thư viện Python khác. Bạn có thể sử dụng ứng dụng để thực hiện các tác vụ như tìm kiếm dữ liệu, hiển thị biểu đồ, v.v.

## Cài Đặt Các Thư Viện Cần Thiết

### Cách 1: Cài Đặt Tất Cả Các Thư Viện Tự Động

Ứng dụng đã tích hợp một chức năng tự động kiểm tra và cài đặt các thư viện thiếu. Để sử dụng tính năng này, bạn chỉ cần làm theo các bước sau:

1. **Tải về và giải nén mã nguồn của ứng dụng** vào máy tính của bạn.
2. **Mở Command Prompt (CMD)**:
    - Trên Windows, bạn có thể tìm kiếm "cmd" trong Start Menu và mở Command Prompt/ or Ctr + '`': mở terminal trên VS Code.
3. **Di chuyển đến thư mục chứa mã nguồn** của ứng dụng bằng lệnh `cd`:
    ```bash
    cd đường_dẫn_đến_thư_mục_chứa_mã_nguồn
    ```
4. **Chạy ứng dụng**:
    - Nhập lệnh sau để chạy ứng dụng:
    ```bash
    python tên_tệp.py
    ```
    (Thay `tên_tệp.py` bằng tên tệp Python của bạn).

Ứng dụng sẽ tự động kiểm tra và cài đặt tất cả các thư viện thiếu, sau đó khởi động giao diện người dùng (GUI).

### Cách 2: Cài Đặt Các Thư Viện Thủ Công

Nếu bạn muốn cài đặt các thư viện thủ công trước khi chạy ứng dụng, bạn có thể làm theo các bước sau:

1. **Tải về và giải nén mã nguồn của ứng dụng**.
2. **Mở Command Prompt (CMD)** và di chuyển đến thư mục chứa mã nguồn của ứng dụng.
    ```bash
    cd đường_dẫn_đến_thư_mục_chứa_mã_nguồn
    ```
3. **Cài đặt các thư viện cần thiết**:
    - Chạy các lệnh sau để cài đặt từng thư viện:
    ```bash
    pip install pandas
    pip install matplotlib
    pip install pillow
    pip install tkinter  # Tkinter có thể có sẵn với Python
    ```
4. **Chạy ứng dụng**:
    Sau khi cài đặt các thư viện, bạn có thể chạy ứng dụng bằng lệnh:
    ```bash
    python main.py
    ```

## Cách Sử Dụng Ứng Dụng

1. **Khởi Động Ứng Dụng**: Sau khi chạy ứng dụng, bạn sẽ thấy cửa sổ GUI mở ra. Ứng dụng sẽ yêu cầu bạn đăng nhập hoặc thực hiện các thao tác tùy thuộc vào tính năng bạn muốn sử dụng.
   
2. **Tìm Kiếm Dữ Liệu**: Bạn có thể nhập các giá trị để lọc và tìm kiếm dữ liệu trong ứng dụng. Chỉ cần nhập tên trường và giá trị cần tìm, sau đó nhấn nút "Tìm kiếm".

3. **Hiển Thị Biểu Đồ**: Nếu ứng dụng hỗ trợ, bạn cũng có thể xem các biểu đồ hoặc đồ thị liên quan đến dữ liệu.

## Lỗi Thường Gặp

- **Lỗi cài đặt thư viện**: Nếu gặp lỗi trong quá trình cài đặt thư viện, hãy kiểm tra kết nối internet và thử lại.
- **Lỗi khi chạy ứng dụng**: Đảm bảo rằng bạn đang sử dụng phiên bản Python phù hợp và đã cài đặt tất cả thư viện cần thiết.

## Liên Hệ

Nếu bạn gặp vấn đề khi sử dụng ứng dụng, vui lòng liên hệ với đội ngũ phát triển qua email: [chuongminh3225@gmail.com](mailto:chuongminh3225@gmail.com).


---

Chúc bạn sử dụng ứng dụng thành công!

