'''
2
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.
Lấy kết quả từ ketqua.net.
Dạng của câu lệnh:
ketqua.py [NUMBER1] [NUMBER2] [...]

Các thư viện:

requests
beautifulsoup4 [tuỳ chọn]
argparse hay sys.argv

Gợi ý:


nargs https://docs.python.org/2/library/argparse.html
'''
import sys
import requests
from bs4 import BeautifulSoup
import json
def get_result():
    today_prices = {}
    you_win = []
    r = requests.get('http://ketqua.net')
    data = r.text
    soup_data = BeautifulSoup(data,'html.parser')
    for results in soup_data.find_all('td')[1:38]:
        if results.string is not None:
            if not results.string.isdigit():
                winning_rank = results.string
                today_prices[winning_rank] = []
            else:
                today_prices[winning_rank].append(results.string)

    for value in today_prices.values():
        for i in value:
            you_win.append(i)
    return you_win

def main():
    final_list = []
    ketqua = get_result()
    option = sys.argv[1:]
    for x in option:
        for y in ketqua:
            if y[-2:] == x[-2:]:
                final_list.append(x)

    if len(final_list) == 0:
        final_list = ketqua

    print(final_list)
    
if __name__ == "__main__":
    main()
