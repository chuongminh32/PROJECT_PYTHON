# ĐỒ ÁN PYTHON 

### Thành viên 1
- **Họ và tên**: Phạm Hàn Minh Chương.
- **MSSV**: 23110187.
- **Vai trò**: Leader, Quản lí dự án, lên kế hoạch, điều phối nhóm, code GUI [FE], làm sạch data (Numpy, Pandas).

### Thành viên 2
- **Họ và tên**: Nguyễn Thanh Bình Minh.
- **MSSV**: 23110266.
- **Vai trò**: BE, Code chức năng CRUD, làm sạch data.

### Thành viên 3
- **Họ và tên**: Nguyễn Thị Thanh Thùy.
- **MSSV**: 23110336.
- **Vai trò**: BE, Vẽ biểu đồ, chuẩn hóa thống nhất data (nếu có), Tester.


* Cấu trúc thư mục đồ án:
project_root/
│
├── data/                           # Thư mục chứa tập tin dữ liệu
│   ├── dataset.csv                 # Tập dữ liệu nguồn
│   └── cleaned_data.csv            # Tập dữ liệu đã làm sạch (sau khi xử lý)
│
├── modules/                        # Thư mục chứa các modules theo chức năng
│   ├── __init__.py                 # Tập tin để biến "modules" thành một package
│   ├── data_cleaning.py            # Module xử lý làm sạch dữ liệu
│   ├── data_normalization.py       # Module xử lý chuẩn hóa dữ liệu
│   ├── data_crud.py                # Module thực hiện các thao tác CRUD
│   ├── data_visualization.py       # Module trực quan hóa dữ liệu
│   └── utils.py                    # Các hàm tiện ích dùng chung cho nhiều module
│
├── gui/                            # Thư mục chứa các tập tin giao diện 
│   └── main_gui.py                 # Chương trình giao diện chính (dùng Tkinter)
│
├── tests/                          # Thư mục chứa các tập tin kiểm thử (optional)
│   ├── test_cleaning.py            # Kiểm thử module làm sạch dữ liệu
│   ├── test_crud.py                # Kiểm thử module CRUD
│   └── test_visualization.py       # Kiểm thử module trực quan hóa dữ liệu
│
├── main.py                         # Chương trình chính để chạy dự án
├── requirements.txt                # Danh sách thư viện phụ thuộc (Numpy, Pandas,...)
└── README.md                       # Tập tin hướng dẫn sử dụng
