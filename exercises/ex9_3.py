"""
3
Viết script lấy top N câu hỏi được vote
cao nhất của tag LABEL trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất
Link API: https://api.stackexchange.com/docs
Dạng của câu lệnh:

so.py N LABEL
"""
import sys
import requests
import json
def top_tags(N,LABEL):
    path = "https://api.stackexchange.com/2.2/questions?order=desc&sort=votes""&tagged=" + LABEL + "&site=stackoverflow"
    resp= requests.get(path)
    data = resp.json()
    for i in range(1,N):
        print(i,'Score -',data['items'][i]['score'],':'+'questions:',data['items'][i]['title']+'--->','link to answer:',data['items'][i]['link'])
    
def main():

    print(top_tags(int(sys.argv[1]),sys.argv[2]))

if __name__ == "__main__":
    main()