'''
5
Đọc file CSV dientich.csv (trong thư mục này) bằng pandas: pd.read_csv()
Tìm ra 10 tỉnh có diện tích lớn nhất Việt Nam năm 2015.
Vẽ đồ thị cột (bar) diện tích của 10 tỉnh đó.
(dữ liệu lấy từ tổng cục thống kê Việt Nam: https://www.gso.gov.vn/default.aspx?tabid=714 chọn "Diện tích, dân số và mật độ dân số phân theo địa phương").
Gợi ý:
để đồ thị có thể ghi tiếng Việt, sử dụng font Unicode như "Arial":
matplotlib.rc('font', family='Arial')
'''
import pandas as pd
import matplotlib.pyplot as plt
import pylab

df = pd.read_csv('dientich.csv',sep=';',header=2)
df.rename(columns={' ':'Geographical','Diện tích(*) (Km2)':'acreage_2011','Diện tích(*) (Km2).1':'acreage_2012', 'Diện tích(*) (Km2).2':'acreage_2013','Diện tích(*) (Km2).3':'acreage_2014','Diện tích(*) (Km2).4':'acreage_2015'},inplace=True)
df_chosen = df.iloc[:,[0,-1]]
df_sort = df_chosen.sort_values('acreage_2015',ascending=False)[0:10]
try:
    df_sort.to_csv('result.csv')
except UnicodeEncodeError:
    pass
plt.rc('font',family='Arial')
df_sort.plot.bar('Geographical')
pylab.show()