import re
t="I am Ravi FROM 9 I am Ravi"
# x=re.findall("a",t)
# # print(x)
# y=re.search("a",t)
# print(y.start())
# print(y.span())
# x=re.findall("[a-m,A-Z,0-9]",t)
# y=re.search("[0-9]",t)
# print(x)
# print(y.span())
#FIND ALL DIGITS
# x=re.findall("\d",t)
# print(x)
# y=re.search("\d",t)
# print(y.start())

# x=re.findall(".",t)
# print(x)
# y=re.search(".",t)
# print(y.span())

#STARTING
# x=re.findall("^I",t)
# print(x)
# y=re.search("^I",t)
# print(y.start())
# x=re.findall("9$",t)
# print(x)


# x=re.findall("ax*",t)
# y=re.findall("ax+",t)
# z=re.findall("am{2}",t)
# print(z)


# x=re.findall("Ravi|prasad",t)
# print(x)

# x=re.findall("\AI",t)
# print(x)
#
# x=re.findall(r"i\b",t)
# print(x)

x=re.findall(r"\Bavi",t)
print(x)








































