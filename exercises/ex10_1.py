'''
1
Làm một website tuyển dụng.
Lấy dữ liệu các job từ: https://github.com/awesome-jobs/vietnam/issues
Lưu dữ liệu vào một bảng jobs trong SQLite. Xem ví dụ: https://docs.python.org/3/library/sqlite3.html
Dùng Flask tạo website hiển thị danh sách các jobs khi vào đường dẫn /.
Khi bấm vào mỗi job (1 link), sẽ mở ra trang chi tiết về jobs (giống như trên
các trang web tìm viêc).
'''
import json
from flask import Flask, render_template, request, Markup
from flask import Flask, render_template, Markup
import sqlite3
import markdown

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect('awesome-jobs-vn.db')
    titles = c.execute('SELECT id, title FROM jobs;').fetchall()
    return render_template('index.html', titles=titles)


@app.route('/<string:id>')
def jobs_details(id=None):
    conn = sqlite3.connect('awesome-jobs-vn.db')
    c = conn.cursor()
    body = c.execute('''SELECT title, body FROM jobs where id = '{}';'''.format(id)).fetchall()
    body = c.execute('''SELECT title, body FROM jobs where id = '{}';
                     '''.format(id)).fetchall()
    title = body[0][0]
    body = Markup(markdown.markdown(body[0][1]))
    return render_template('job-detail.html',
                           title=title,
                           body=body)


if __name__ == '__main__':
    app.run(debug=True)