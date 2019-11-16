#!/usr/bin/env python3

__doc__ = '''
Chuẩn bị cho buổi sau
---------------------

- Cài đặt virtualenv, dùng nó tạo virtualenv cho Python3 (-p python3)
- Xem trong thư mục ``env`` vừa tạo có gì.
  https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
- Activate môi trường vừa tạo, dùng pip cài đặt các thư viện phổ biến::

  ```
  pip install requests six pep8 flake8 ipython ipdb numpy pandas scipy \
              matplotlib jupiter flask
  ```
'''


def main():
    print(__doc__)


if __name__ == "__main__":
    main()
