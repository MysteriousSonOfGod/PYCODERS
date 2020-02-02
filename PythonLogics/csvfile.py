import csv
# path="data.csv"
# lines=[i for i in open(path)]
# print(lines[0].strip().split(','))
# stri="Ravi Prasad Kalyan"
# print(stri.strip().split(' '))


#USING CSV MODULE
path="data.csv"
file=open(path, newline='')
reader=csv.reader(file)

header=next(reader)
data=[row for row in reader]
print(header)
print(data[0])