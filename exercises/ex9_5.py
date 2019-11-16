'''
5
[Nâng cao]
Sử dụng requests viết một script lấy toàn bộ thông tin các Page của
các quán cafe, trà ở trung tâm Hà Nội bằng Facebook Graph API.
Các từ khóa: "coffee", "tea", "cafe", "caphe", "tra da".
Tọa độ: 21.027875, 105.853654 với bán kính là 1km.
Trả về kết quả bao gồm name, id, location, website của mỗi Page.

Hướng dẫn dùng Facebook API:

https://developers.facebook.com/docs/graph-api/using-graph-api#search

Sử dụng Grapth API Explorer để thử:

https://developers.facebook.com/tools-and-support/

Sử dụng App ID và App Secret sau để lấy token:

App ID: 1537101179929447
App Secret: 4da789d9de5f279a58051e629a4c6ef3

Hướng dẫn tạo Token:

https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens
Chú ý:

Để ý đến phần paging của mỗi response trả về. Hãy bấm vào đó để xem chuyện gì

sẽ xảy ra.

Kết quả trả về xuất ra một file hanoi_coffee.json.
Hãy sử dụng option indent cho function json.dump()
'''
import requests
import json
import codecs
result = []
def solve():
    # getting access_token codes
    Base_URL = 'https://graph.facebook.com/v2.9/'
    app_id = '1537101179929447'
    app_secret = '4da789d9de5f279a58051e629a4c6ef3'
    token_path = 'oauth/access_token?client_id={0}&client_secret={1}&grant_type=client_credentials'.format(app_id,app_secret)
    path_1 = Base_URL + token_path
    r1 = requests.get(path_1)
    json_data1 = r1.json()

    # getting name,id,'paging''next' 
    token_access = json_data1['access_token']
    search_path = 'search?type=place&query={0}&center=21.027875,105.853654&distance=1000&fields=id,name,website,location&access_token={1}'
    query = ['cafe','coffee','caphe','trada','tea']
    for item in query:
        path_2 = Base_URL + search_path.format(item,token_access)
        r2 = requests.get(path_2)
        json_data2 = r2.json()
        result.extend(json_data2['data'])

    # using 'paging, next' for link_api to search
    link_api =json_data2['paging']['next']
    json_data2 = requests.get(link_api).json()
    result.extend(json_data2['data'])

    big_data = json.dumps(result,ensure_ascii=False)
    with codecs.open('hanoi_coffee.json','w',encoding='utf-8') as f:
        f.write(big_data)
        f.write('\n')
    f.close()

solve()
