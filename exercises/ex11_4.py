'''
4
Tạo 1000 dữ liệu kiểu int ngẫu nhiêu gắn với 1000 ngày từ 09/02/2010.
Dùng kiểu pd.Series.
Tính cumsum() và vẽ đồ thị.
'''
def solve():
    import pandas as pd
    import numpy as np
    import numpy.random as nprnd
    import matplotlib.pyplot as plt
    import pylab
    df = pd.DataFrame({'A':pd.date_range('2010/2/9',periods=1000),'B':pd.Series(np.random.randint(0,1000,size=1000))})
    df.hist()
    pylab.show()
    df.loc['Total'] = pd.Series(df['B'].sum(),index=['B'])
    print(df)
solve()