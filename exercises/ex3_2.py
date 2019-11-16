#!/usr/bin/env python3

data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''
# https://www.poetrysoup.com/poem/cross_my_heart_609765

def solve(text):
    '''Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
    Chỉ viết hoa chữ cái đầu tiên.
    '''
    lst = []
    for char in text.strip().split('\n'):
        lst.append(char[0])
    result = ''.join(lst)
    return result.capitalize()

def main():
    '''
    Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    '''
    text = data
    print(solve(text))

if __name__ == "__main__":
    main()