import sys
# print(sys.version)
# print(sys.version_info)
# print(type(sys))
# print(sys.argv)
# The sys module provides information about constants, functions and methods of the Python interpreter.
# dir(system) gives a summary of the available constants, functions and methods.
# Another possibility is the help() function. Using help(sys) provides valuable detail information.
#
# The module sys informs e.g. about the maximal recursion depth (sys.getrecursionlimit() ) and provides the possibility to change (sys.setrecursionlimit())
# The current version number of Python can be accessed as well:
# or it can be iterated via a for loop:

# for i in range(len(sys.argv)):
    # if i == 0:
    #     print ("Function name: %s" % sys.argv[0])
    # else:
    #     print ("%d. argument: %s" % (i,sys.argv[i]))


# print(sys.getrecursionlimit())
# import os
# command='sudo su - '
# print('Ravi@143')
# os.system(command)

import os

command = " "
while (command != "exit"):
    command = input("Command: ")
    handle = os.popen(command)
    line = " "
    while line:
        line = handle.read()
        print(line)
    handle.close()

print ("Ciao that's it!")
