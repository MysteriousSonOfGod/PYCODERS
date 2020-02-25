import pandas as pd
# series1 = pd.Series([1, 2, 3, 4], index=['a','b','c','d'])
# print(series1)

#Creating a DataFrame from a list of lists:

# list_of_lists = [['apple',10],['mango',12],['banana',13]]
# for i in list_of_lists:
#     print(i)
# df = pd.DataFrame(list_of_lists,columns=['fruit','count'],dtype=int)
# print(df)


#Creating a DataFrame from a dictionary:

import matplotlib.pyplot as plt
emp = ['Parker', 'John', 'Smith', 'William']
id = [102, 107, 109, 114]
balls = [110, 199, 201, 188]
emp_series = pd.Series(emp)
id_series = pd.Series(id)
nballs = pd.Series(balls)
frame = { 'Name': emp_series, 'Runs': id_series, 'Balls': nballs}
result = pd.DataFrame(frame)
result['Total'] = result['Runs'].sum()
print(result)