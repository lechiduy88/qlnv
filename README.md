----Dự án quản lý nhân viên


-----Có đầy đủ chức năng thêm, sửa, xóa, tìm kiếm


------Cách cài đặt và thiết lập dự án ------
-Database: Sử dụng Mysql được tích hợp trên XAMPP
-Tạo database: create database qlnv
-Tạo bảng employee:
use qlnv
CREATE TABLE employee(
	id int PRIMARY key AUTO_INCREMENT,
    id_employee int UNIQUE,
    name_employee varchar(50),
    group_employee varchar(20),
    start_date varchar(20),
    training_date varchar(20),
    trainer varchar(50),
    training_stage varchar(500),
    comments varchar(500),
    notes varchar(500)
)

Code: Sử dụng framework Flask và các thư viện con để viết 
Chạy bấm F5 file app.py


