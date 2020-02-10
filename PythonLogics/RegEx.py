# # RegEx Functions
# # The re module offers a set of functions that allows us to search a string for a match:
# import re
# #FIND ALL
# txt = "The rain in Spain"
# x=re.findall("k", txt)#IF KEY NOT FOUND IN THE STRING THE RESULT IS EMPTY LIST
# print(x)
#
#
#
# # The search() Function
# # The search() function searches the string for a match, and returns a Match object if there is a match.
# #
# # If there is more than one match, only the first occurrence of the match will be returned:
#
# txt = "The rain in Spain"
# x = re.search("k", txt)#IF THE SEARCH IS NOT FOUND IN THE STRING THE RESULT IS none
# print(x)
#
# import re
#
# #Replace all white-space characters with the digit "9":
#
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
#
# txt = "The rain in Spain"
# x = re.search(r"\bT\w+", txt)
# print(x.span())
#
#
# import re
#
# txt = "Ravi@143"
#
# #Find all lower case characters alphabetically between "a" and "m":
#
# x = re.findall("[a-zA-Z]", txt)
# print(x)
#
#
# import re
#
# txt = "hello world"
#
# #Check if the string ends with 'world':
#
# x = re.findall("world$", txt)
# print(x)

#
#
# import re
#
# txt = "Ravi@143"
#
# x = re.findall("[@],[0-9]", txt)
# print(x)


# Primary conditions for password validation :
#
# Minimum 8 characters.
# The alphabets must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].
# Examples:

import re
name="Kalyan@143"
if len(name)>8:
    if re.findall("[0-9]", name):
        if re.findall("[A-Z]", name):
            if re.findall("[a-z]",name):
                print("yes")
else:
    print("Imvalid")