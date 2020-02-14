try:
    l=[1,2,3,4,5,"ravi",2.4]
    l2=[2,3,4]
    # print(l)
    # for i in l:
    #     print(i)
    print(l[::])
    print(l[2:])
    print(l[::-1])
    print(2 in l)
    print(max(l))
except TypeError:
    print("error")