# Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:
# Ví dụ với user hvnsweeting, sử dụng dữ liệu ở JSON format tại
# https://api.github.com/users/hvnsweeting/repos
# Câu lệnh của chương trình có dạng:
# githubrepos.py username

# Gợi ý:
# Sử dụng các thư viện:

# requests
# sys or argparse

import sys

import requests
def get_repos(username):
    result = []
    used_link = 'https://api.github.com/users/{0}/repos'
    data = requests.get(used_link.format(username))
    repos = data.json()
    result =[d['name'] for d in repos]
    return result

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
        print(get_repos(username))
    else:
        print('no_username')

if __name__ == '__main__':
    main()