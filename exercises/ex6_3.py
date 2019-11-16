#!/usr/bin/env python3

import csv
import os
import time

def find_max_price(datafile):
    f = open(datafile)
    dr = csv.DictReader(f, ['time', 'price', 'UNKNOWN']) # NOQA
    line_max , value_max = {},0
    for idx,line in enumerate(dr):
        # t = time.gmtime(int(line['time']))
        price = float(line['price'])
        if value_max < price:
            value_max = price
            line_max = line
    print(time.gmtime(int(line_max['time'])))
    print(value_max)

def solve():
    '''Tìm ngày giá BTC lên cao nhất. Trả về Tuple chứa ngày ở định dạng
    YYYY-mm-dd (VD: 2017-06-19) và giá VND của 1 BTC
    '''
    # http://api.bitcoincharts.com/v1/csv/
    datafile = 'localbtcVND.csv'
    exdir = os.path.dirname(__file__)
    datapath = os.path.join(exdir, datafile)

    result = find_max_price(datapath)
    return result

def main():
    now = time.gmtime(int(time.time()))
    print(now.tm_year, now.tm_mon, now.tm_mday)
    print(solve())


if __name__ == "__main__":
    main()