import json
# f=open('ravi.json','r')
# r=f.read()
# x=json.loads(r)
# print(dict(x))

# f = open("ravi.json", 'r')
# r = f.read()
# x = json.loads(r)
# li2 = [(kk, vv) for kk, vv in x.items()]
# print(li2)

# li=[]
# with open('ravi.txt','r') as f:
#     for i in f:
#         val=i.split(',')
#         li.extend(val)
#         val=i.split('\n')
#         li.extend(val)
# print(li)
# y=[]
# with open("ravi.txt") as f:
#     for line in f:
#         (key, val) = line.split()
#         y[key] = val
# li3 = [(k, v) for k, v in dict(y).items()]
# print(li3)

# def txt():
#     d = {}
#     with open("ravi.txt") as f:
#         for line in f:
#             (key, val) = line.split()
#             d[key] = val
#     return d
#
# r=txt()
# print(r)

# import pandas
# td=pandas.read_csv('ravi.txt', header=None)
# print(td)
# # for i,j in td.items():
# #     print(i,j)
# import pandas as pd
# # data = pd.read_csv('ravi.txt', sep=" ", header=None)
# # print(data)
# df = pd.read_fwf('ravi.txt')
# print(df)


# import pandas as pd
# dataset=pd.read_csv("ravi.txt",delimiter="\t")
# print(dataset)

import pandas as pd

data = pd.read_csv('../ravi.txt', header = None)
print(data)


















