d={"Name":"Ravi", "Surname":"Sanaboina", "Id":9652762676}
# print(d)
# for i, j in d.items():
#     print(i,j)
#
# for key in d.values():
#     print(key)

x=d.get("Name")
print(x)

y=d.get("Id")
print(y)

#Try to return the value of an item that do not exist:
z=d.get("price",15000)
print(z)