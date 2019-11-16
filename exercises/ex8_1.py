#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Lưu file ``https://raw.githubusercontent.com/hvnsweeting/
states/master/salt/event/init.sls`` về máy với tên event.yaml

- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
 `pickle.dump` nội dung, ghi ra một file tên là event.json

- Dùng thư viện pickle và pickle.dump nội dung trên ra file event.pkl. Chú
ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc thêm tại đây:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
'''


import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA
import requests


def your_function():
    '''Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    '''
    content = requests.get('https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls')
    str_content = content.text
    with open('event.yaml','w') as f:
        yaml.dump(str_content,f)
    f.close()

    with open('event.yaml') as f:
        yaml_data = yaml.load(f)
        print(yaml_data,type(yaml_data))
    f.close()

    with open('event.json','w') as f:
        json.dump(str_content,f)
    f.close()

    with open('event.json') as f:
        json_data = json.load(f)
        print(json_data,type(json_data))
    f.close()

    with open('event.pkl','wb') as f:
        pickle.dump(str_content,f)
    f.close()

    with open('event.pkl','rb') as f:
        pickle_data = pickle.load(f)
        print(pickle_data,type(pickle_data))
    f.close()

def solve():
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    '''
    result = your_function()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
