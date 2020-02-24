#--------------------------------------------------------FIND DESTINATION FILE------------------------------------------
# import os
#
# findfile="find ~/Downloads/extra/ -iname *ravi*.xlsx"
# r=os.system(findfile)

#-------------------------------------------------------CREATE NEW FILE-------------------------------------------------

# import os
# print("Please Enter The File Name")
# n=input()
# cmd="touch {}.py".format(n)
# os.system(cmd)

#-------------------------------------------------------DELETE FILE-----------------------------------------------------

# import os
# print("--------------------------Enter The File Name----------:")
# name=input()
# cmd="rm {}.py".format(name)
# os.system(cmd)

#-------------------------------------------------------Copy file-------------------------------------------------------
import os
print("------------Enter Source File:------------------")
sou=input()
des=input()
cmd="cp {} {}".format(sou,des)
os.system(cmd)
#/home/ravi/Documents/PYCODERS/ShellScripting
#/home/ravi/Documents/PYCODERS/ShellScripting/Shell Commands

#--------------------------------------------------------