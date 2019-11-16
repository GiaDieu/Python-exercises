'''4
Viết script lấy về 50 kết quả đầu tiên tìm được với từ khoá "coffee"
quanh toạ độ 10.779614, 106.699256 (nhà thờ Đức Bà - HCM) với bán kính 5KM.
Ghi kết quả theo định dạng JSON vào file hcm_coffee.json. (hoặc lưu vào 1 SQLite DB)
Sử dụng Google Map API
https://developers.google.com/places/web-service/
Chú ý: phải tạo "token" để có thể truy cập API.
'''
import requests
import json
import codecs
def solve():
    API_1 ='AIzaSyBP6EnJfHjbuoXY3D2QawSaSjNdSQmr6tM'
    API_2 = 'AIzaSyAgPad8-klIGH0hWbDwD7VAMn-kyl0FG4g'
    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=10.779614,106.699256&radius=5000&keyword=coffee&key={0}'
    token_link = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=10.779614,106.699256&radius=5000&keyword=coffee&key={0}&pagetoken={1}'
    
    result = []
    # get 20 lists_for first API call
    link_add_key_1 = URL.format(API_1)
    r1 = requests.get(link_add_key_1)
    json_data1 = r1.json()
    for x in json_data1['results']:
        result.append(x['name'])

    # get more 20 lists for second API call
    link_add_key_2 = URL.format(API_2)
    r2 = requests.get(link_add_key_2)
    json_data2 = r2.json()
    for y in json_data2['results']:
        result.append(y['name'])

    # get other 20 lists for pagetoken using API_2 call
    page_token = token_link.format(API_2,json_data2['next_page_token'])
    r3 = requests.get(page_token)
    json_data3 = r3.json()
    for z in json_data3['results']:
        result.append(z['name'])

    final_list = result[0:50]
    final_data = json.dumps(final_list)
    with codecs.open('hcm_coffee.json','w') as f:
        f.write(final_data)
  
def main():
    print(solve())

if __name__ == "__main__":
    main()