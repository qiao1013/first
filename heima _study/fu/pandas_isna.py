#空值判断操作
#isna()判断是否是空值
import pandas as pd
import numpy as np
print(pd.isna(None))
print(pd.isna(np.nan))
print(pd.isna(pd.NA))

#是否不是空值
 
print(pd.notna(None))
print(pd.notna(np.nan))
print(pd.notna(pd.NA))

#读取文件
df1 = pd.read_csv(r'C:\Users\乔\Desktop\python\heima _study\data\survey_visited.csv',encoding='gbk')
print(df1['ident'])
print(df1)

