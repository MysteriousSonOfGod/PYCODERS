import os

findfile="find ~/Downloads/extra/ -iname *ravi*.xlsx"
r=os.system(findfile)
print(r)