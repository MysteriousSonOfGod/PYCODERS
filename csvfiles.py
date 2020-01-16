#using csv module
# import csv
# # d=[]
# with open('ram.csv', newline='') as csvfile:
#     spamreader=csv.reader(csvfile)
#     for i in spamreader:
#         print(', '.join(i))#using .join function
#         d.extend(i)
# it=iter(d)
# rd=dict(zip(it, it))
# for i,j in rd.items():
#     print(i,j)

# import pandas
# dd=pandas.read_csv('ram.csv')
# print(dd)

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# df = pd.read_excel('exfile.xls')
#
# print("Column headings:")
# print(df.columns)
# import xlrd
# wb = xlrd.open_workbook("exfile.xls")
# sh = wb.sheet_by_index(0)
# print(sh.cell(0,0).value)

# import pandas
# df=pandas.read_json('ravi.json')
# print(df)

import pandas as pd
import numpy as np
b=[]
info=np.array(['R','a','v','i'])
a=pd.Series(info)
x=b.append(a)
print(b)

















