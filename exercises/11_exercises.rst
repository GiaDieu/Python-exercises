11. Scipy
=========

.. note::

  Học viên làm bài vào file `.py`, không nộp file Jupyter notebook.
  File Jupyter notebook có thể paste lên http://gist.github.com/ để nộp kèm
  link làm kết quả của bài tập.

1
-

Dùng numpy để tạo các ma trận sau::

	array([[ 0,  1,  2,  3,  4,  5],
	       [10, 11, 12, 13, 14, 15],
	       [20, 21, 22, 23, 24, 25],
	       [30, 31, 32, 33, 34, 35],
	       [40, 41, 42, 43, 44, 45],
	       [50, 51, 52, 53, 54, 55]])


	array(  [[0., 0., 0., 0., 0.],
			 [2., 0., 0., 0., 0.],
			 [0., 3., 0., 0., 0.],
			 [0., 0., 4., 0., 0.],
			 [0., 0., 0., 5., 0.],
			 [0., 0., 0., 0., 6.]])

2
-

Vẽ đồ thị hàm sin,cos,tan trong khoảng -2𝜋 -> 2𝜋


3
-

Vẽ đồ thị hàm x = y**2 và x = y trên cùng 1 trục toạ độ.

4
-

Tạo 1000 dữ liệu kiểu int ngẫu nhiêu gắn với 1000 ngày từ 09/02/2010.
Dùng kiểu pd.Series.

Tính cumsum() và vẽ đồ thị.

5
-

Đọc file CSV dientich.csv (trong thư mục này) bằng pandas: pd.read_csv()
Tìm ra 10 tỉnh có diện tích lớn nhất Việt Nam năm 2015.
Vẽ đồ thị cột (bar) diện tích của 10 tỉnh đó.

(dữ liệu lấy từ tổng cục thống kê Việt Nam: https://www.gso.gov.vn/default.aspx?tabid=714 chọn "Diện tích, dân số và mật độ dân số phân theo địa phương").

Gợi ý:
để đồ thị có thể ghi tiếng Việt, sử dụng font Unicode như "Arial"::

	matplotlib.rc('font', family='Arial')

6
-

- Viết review cho PyFML https://www.facebook.com/pyfml/
