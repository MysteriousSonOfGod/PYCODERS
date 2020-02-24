#---------------------------------------------------CREATING Text File--------------------------------------------------

# textfile=open("myfile.txt",'x')
# print(textfile.read())
# textfile.close()


#---------------------------------------------------Writing DATA--------------------------------------------------------

# textfile=open("myfile.txt",'w')
# textfile.write('This is ravi prasad')
# textfile.close()

#---------------------------------------------------Reading DATA--------------------------------------------------------

# text=open("myfile.txt","r")
# data=text.readline()
# print(data)

#---------------------------------------------------FROM INPUT----------------------------------------------------------

# print("---------------------Enter the number of lies-----------------------")
# n=int(input())
# c=0
# while c<n:
#     print("-----------------------------Enter Data----------------------------------")
#     m = input()
#     f=open("myfile.txt","a")
#     f.write(m)
#     c+=1


#-------------------------------------Writing python output to the files------------------------------------------------
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))
