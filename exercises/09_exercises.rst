9. Crawling
===========

Từ chương này, bài làm sau khi chỉnh sửa sạch sẽ, có thể đưa lên GitHub
để tạo profile đẹp cho học viên, tiện cho xin việc sau này.

- Đăng ký GitHub rồi tạo repo và push code lên, xem thêm hướng dẫn tại
  https://pymivn.github.io/vinagit/ và https://help.github.com/
- Dùng GitHub là gợi ý cho các học viên muốn trở thành lập trình viên
  và xin việc lập trình sau khi làm, không bắt buộc.
- Các API có thể yêu cầu người dùng tạo tài khỏan và sử dụng "token". Token
  là một string dài, cấp cho người dùng để họ dùng với code, chứng minh mình là
  một user hợp lệ (thay vì dùng username/password truyền thống).
  Với các public API không bắt buộc dùng token, khi sử dụng token, user sẽ
  thường có quyền truy cập API nhiều request/ngày hơn so với không dùng.
- Token hay user/password là những thông tin cần được bảo mật, không viết vào
  code rồi push lên mạng - sử dụng file text để chứa thông tin (JSON/text/YAML
  ...) hay https://docs.python.org/3/library/configparser.html
  và không push file này lên. Hoặc cách khác là sử dụng biến environment (truy
  cập qua os.environ) https://docs.python.org/3/library/os.html#os.environ,
  set biến environment:
  http://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html

1
-

Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

Ví dụ với user ``hvnsweeting``, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/hvnsweeting/repos

Câu lệnh của chương trình có dạng::

  githubrepos.py username

Gợi ý:

Sử dụng các thư viện:

- requests
- sys or argparse

2
-

Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]

Các thư viện:

- requests
- beautifulsoup4 [tuỳ chọn]
- argparse hay sys.argv

Gợi ý:

- ``nargs`` https://docs.python.org/2/library/argparse.html

3
-

Viết script lấy top **N** câu hỏi được vote cao nhất của tag **LABEL** trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

  so.py N LABEL

4
-

Viết script lấy về 50 kết quả đầu tiên tìm được với từ khoá "coffee"
quanh toạ độ 10.779614, 106.699256 (nhà thờ Đức Bà - HCM) với bán kính 5KM.
Ghi kết quả theo định dạng JSON vào file hcm_coffee.json. (hoặc lưu vào 1 SQLite DB)

Sử dụng Google Map API
https://developers.google.com/places/web-service/

Chú ý: phải tạo "token" để có thể truy cập API.

5
-

[Nâng cao]
Sử dụng ``requests`` viết một script lấy toàn bộ thông tin các Page của
các quán cafe, trà ở trung tâm Hà Nội bằng **Facebook Graph API**.

Các từ khóa: ``"coffee", "tea", "cafe", "caphe", "tra da"``.

Tọa độ: ``21.027875, 105.853654`` với bán kính là ``1km``.

Trả về kết quả bao gồm ``name, id, location, website`` của mỗi Page.

- Hướng dẫn dùng Facebook API:

https://developers.facebook.com/docs/graph-api/using-graph-api#search

- Sử dụng Grapth API Explorer để thử:

https://developers.facebook.com/tools-and-support/

- Sử dụng App ID và App Secret sau để lấy token:

``App ID: 1537101179929447``

``App Secret: 4da789d9de5f279a58051e629a4c6ef3``

- Hướng dẫn tạo Token:

https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens

**Chú ý**:

- Để ý đến phần paging của mỗi response trả về. Hãy bấm vào đó để xem chuyện gì
sẽ xảy ra.

- Kết quả trả về xuất ra một file ``hanoi_coffee.json``.

- Hãy sử dụng option ``indent`` cho function ``json.dump()``

Chuẩn bị cho buổi sau
---------------------

- Đăng ký LinkedIn
- Đăng ký nhận mail tin tức Python http://www.pythonweekly.com/
- Xem các bài viết tag Python trên http://www.familug.org/
