#!/usr/bin/env python3

import re
def solve(text):
    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Bé lên 3 bé đi lớp 4' -> [3, 4]
    '''

    result = []
    value = re.findall('\d+',text)
    for i in value:
        result.append(int(i))
    return result

def main():
    ss = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'

    print(solve(ss))
    assert solve(ss) == [60, 20, 0]


if __name__ == "__main__":
    main()
