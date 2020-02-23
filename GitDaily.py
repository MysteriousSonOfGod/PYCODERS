import os
cmd1="git add ."
os.system(cmd1)
n=input("Enter comment")
cmd2="git commit -m {}".format(n)
os.system(cmd2)
cmd3="git push"
os.system(cmd3)