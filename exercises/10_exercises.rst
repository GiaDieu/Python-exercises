10. Web
=======

- Code sau khi hoàn thành, có thể cho "chạy thật", việc "chạy thật" này gọi là
  "deployment" - triển khai cài đặt. Tài liệu Flask có hướng dẫn các option để
  deploy Flask app: http://flask.pocoo.org/docs/0.12/deploying/
- Viết các câu lệnh SQL về lâu dài sẽ trở thành 1 công việc nhàm chán (tạo/sửa
  /xóa) hàng trăm object ... Khi làm việc với những ứng dụng như vậy, người
  ta thường sử dụng một "thư viện" để chuyển đổi qua lại giữa SQL và Python
  object và gọi là ORM (object relation map), Django có sẵn Django ORM, Flask
  thường dùng SQLAlchemy.

1
-
Làm một website tuyển dụng.

Lấy dữ liệu các job từ: https://github.com/awesome-jobs/vietnam/issues

Lưu dữ liệu vào một bảng ``jobs`` trong SQLite. Xem ví dụ: https://docs.python.org/3/library/sqlite3.html

Dùng Flask tạo website hiển thị danh sách các jobs khi vào đường dẫn ``/``.
Khi bấm vào mỗi job (1 link), sẽ mở ra trang chi tiết về jobs (giống như trên
các trang web tìm viêc).

2
-

Crawl tất cả các bài viết có label
Python(http://www.familug.org/search/label/Python), Command, sysadmin và 10 bài
viết mới nhất ở homepage của http://www.familug.org/

Tạo file `index.html`, chứa 4 cột tương ứng cho:

```
Python | Command | Sysadmin | Latest
```

Mỗi cột chứa các link bài viết, khi bấm vào sẽ mở ra bài gốc tại FAMILUG.org

Tham khảo giao diện tại:
- https://themes.getbootstrap.com/
- http://getskeleton.com/#examples

Push code lên GitLab repo, tạo 1 GitLab Page để view kết quả.
https://pages.gitlab.io/

Nâng cao: push code lên GitHub và tạo 1 GitHub Page: https://pages.github.com/

3
-

Làm theo ví dụ tại http://flask.pocoo.org/docs/0.12/tutorial/
Push code cuối cùng lên GitHub.com<div></div>
